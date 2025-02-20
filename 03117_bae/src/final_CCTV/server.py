from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import cv2
import uvicorn
from ultralytics import YOLO
import numpy as np
from collections import defaultdict
import os

app = FastAPI()

# 템플릿 설정 (HTML 파일이 위치한 디렉토리 지정)
templates = Jinja2Templates(directory="templates")

# YOLO11 모델 로드 (객체 감지를 위한 사전 학습된 모델 불러오기)
model = YOLO("yolo11n.pt")

# 객체 추적 기록을 저장하는 딕셔너리 (각 객체 ID별 이동 경로 저장)
track_history = defaultdict(lambda: [])

# 웹캠 설정 (0번 카메라 사용)
cap = cv2.VideoCapture(0)

# 캡처 이미지 저장 폴더 생성 (폴더가 없으면 생성)
CAPTURE_DIR = "captures"
os.makedirs(CAPTURE_DIR, exist_ok=True)

# 홈페이지 엔드포인트 (HTML 페이지 렌더링)
@app.get("/", response_class=StreamingResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 웹캠에서 프레임을 가져와 스트리밍하는 함수
def generate_frames():
    while True:
        success, frame = cap.read()  # 웹캠에서 프레임 캡처
        if not success:
            break

        # YOLO 모델을 사용하여 객체 추적 수행
        results = model.track(frame, persist=True, classes=0, tracker='bytetrack.yaml')
        
        # 감지된 객체의 박스 좌표 및 ID 가져오기
        boxes = results[0].boxes.xyxy.cpu() if results[0].boxes is not None else []
        track_ids = results[0].boxes.id.int().cpu().tolist() if results[0].boxes.id is not None else []

        # 감지된 객체에 대한 정보 표시 및 추적 경로 저장
        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = box  # 박스 좌표
            x, y = (x1 + x2) / 2, (y1 + y2) / 2  # 중심 좌표
            track = track_history[track_id]  # 객체의 이동 경로 저장
            track.append((int(x), int(y)))
            if len(track) > 30:  # 최근 30개의 이동 좌표만 저장
                track.pop(0)
            
            # 이동 경로를 녹색 선으로 그림
            points = np.array(track, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(frame, [points], isClosed=False, color=(0, 255, 0), thickness=2)
            
            # 객체의 바운딩 박스와 ID 표시
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.putText(frame, f"id={track_id}", (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

        # 프레임을 JPEG 형식으로 변환하여 스트리밍
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# 비디오 스트리밍 엔드포인트
@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

# 현재 프레임을 캡처하여 저장하는 엔드포인트
@app.post("/capture")
def capture_frame():
    success, frame = cap.read()
    if success:
        # YOLO 모델을 사용하여 객체 감지 수행
        results = model.track(frame, persist=True, classes=0, tracker='bytetrack.yaml')
        
        # 감지된 객체의 박스 좌표 및 ID 가져오기
        boxes = results[0].boxes.xyxy.cpu() if results[0].boxes is not None else []
        track_ids = results[0].boxes.id.int().cpu().tolist() if results[0].boxes.id is not None else []

        # 객체 감지 결과를 프레임에 표시
        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = box  # 박스 좌표
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # 객체 바운딩 박스
            cv2.putText(frame, f"id={track_id}", (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # 캡처된 이미지를 저장
        capture_path = os.path.join(CAPTURE_DIR, "capture.jpg")
        cv2.imwrite(capture_path, frame)
        return JSONResponse(content={"message": "Capture saved", "path": capture_path})
    
    return JSONResponse(content={"message": "Capture failed"}, status_code=500)

# FastAPI 서버 실행 (로컬에서 8000번 포트 사용)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
