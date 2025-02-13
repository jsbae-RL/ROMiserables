from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

# YOLO11 모델 로드
model = YOLO("yolo11n.pt")

# 웹캠(카메라) 캡처 객체 생성
cap = cv2.VideoCapture('./vid1.mp4')

# 프레임의 너비와 높이 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# 비디오 저장을 위한 코덱 설정 (XVID 사용)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./output.avi', fourcc, 30.0, (640, 480))

# 객체 추적 기록을 저장하는 딕셔너리 (각 객체 ID별 이동 경로 저장)
track_history = defaultdict(lambda: [])

# 비디오 프레임을 읽어오는 반복문 실행
while cap.isOpened():
    # 비디오에서 프레임을 읽기
    success, frame = cap.read()

    if success:
        # YOLO11을 사용하여 객체 추적 수행 (프레임 간 지속적으로 추적)
        results = model.track(frame, persist=True, classes = 0, tracker = 'bytetrack.yaml')

        # 객체 박스와 트랙 ID 가져오기
        boxes = results[0].boxes.xyxy.cpu()  # 객체 경계 박스 좌표 (x, y, w, h)
        track_ids = results[0].boxes.id.int().cpu().tolist()  # 객체 ID 리스트

        # YOLO 결과를 시각적으로 표시한 프레임 가져오기
        annotated_frame = results[0].plot()

        # 객체의 궤적(이동 경로) 시각화
        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = box  # 좌상단 좌표(x1, y1), 우하단 좌표(x2, y2)

            x = (x1 + x2) / 2
            y = (y1 + y2) / 2

            # track_history 딕셔너리에 현재 객체의 좌표 추가
            track = track_history[track_id]
            track.append((float(x), float(y)))  # 객체 중심 좌표(x, y) 저장

            # 30프레임 이상이 되면 가장 오래된 좌표 삭제 (메모리 절약)
            if len(track) > 30:
                track.pop(0)

            # 이동 궤적을 그릴 좌표 리스트를 NumPy 배열로 변환
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))

            # OpenCV의 cv2.polylines() 함수를 사용하여 궤적을 그리기
            cv2.polylines(
                annotated_frame,  # 그릴 프레임
                [points],  # 이동 경로 좌표 배열
                isClosed=False,  # 열린 궤적(닫히지 않은 선)
                color=(0, 255, 0),  # 연한 회색 (RGB)
                thickness=10,  # 선 두께
            )

        # 추적 결과가 포함된 프레임을 화면에 출력
        annotated_frame = cv2.resize(annotated_frame, (int(width/2), int(height/2)))
        cv2.imshow("YOLO11 Tracking", annotated_frame)

        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # 영상이 끝나면 루프 종료
        break

# 비디오 캡처 객체 해제 및 창 닫기
cap.release()
out.release()
cv2.destroyAllWindows()
