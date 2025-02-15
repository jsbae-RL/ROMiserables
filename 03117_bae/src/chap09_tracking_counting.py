from collections import defaultdict

import cv2
import numpy as np
from ultralytics import YOLO

# YOLO11 모델 로드
model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture('./vid1.mp4')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./output.avi', fourcc, fps, (int(width/2), int(height/2)))

# 트래킹 기록 저장
track_history = defaultdict(lambda: [])

# ROI(관심 영역) 정의 (x1, y1, x2, y2)
roi = (400, 500, 650, 750)  # ROI 영역 (사각형 좌상단 (x1, y1), 우하단 (x2, y2))

# 비디오 프레임을 반복하여 처리
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model.track(frame, persist=True,  classes = 0, tracker = 'bytetrack.yaml')
        print(results[0].boxes)
        
        # 감지된 객체의 박스 및 트랙 ID 가져오기
        boxes = results[0].boxes.xywh.cpu() # 객체의 중심좌표(xy) 너비 높이
        track_ids = results[0].boxes.id.int().cpu().tolist()

        # 프레임에 결과 시각화
        annotated_frame = results[0].plot()
        
        # ROI 영역 그리기
        cv2.rectangle(annotated_frame, (roi[0], roi[1]), (roi[2], roi[3]), (0, 255, 0), 2)

        count_in_roi = 0

        # 감지된 객체 처리
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y)))  # 객체 중심 좌표 추가
            print(track)
            if len(track) > 30:
                track.pop(0)

            # 트래킹 경로 그리기
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(
                annotated_frame,
                [points],
                isClosed=False,
                color=(0, 250, 0),
                thickness=10,
            )

            # 객체의 네 꼭짓점 좌표 계산
            x1, y1 = x - w / 2, y - h / 2
            x2, y2 = x + w / 2, y - h / 2
            x3, y3 = x - w / 2, y + h / 2
            x4, y4 = x + w / 2, y + h / 2

            # 네 꼭짓점이 모두 ROI 내부에 있는지 확인
            if (roi[0] < x1 < roi[2] and roi[1] < y1 < roi[3] and
                roi[0] < x2 < roi[2] and roi[1] < y2 < roi[3] and
                roi[0] < x3 < roi[2] and roi[1] < y3 < roi[3] and
                roi[0] < x4 < roi[2] and roi[1] < y4 < roi[3]):
                count_in_roi += 1

        # ROI 내 객체 개수 표시
        if count_in_roi > 0:
            cv2.rectangle(annotated_frame, (roi[0], roi[1]), (roi[2], roi[3]), (0, 0, 255), 5)
            cv2.putText(
                annotated_frame,
                f"count in ROI: {count_in_roi}",
                (roi[0], roi[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                5,
            )
        
        # 시각화된 프레임 출력
        annotated_frame = cv2.resize(annotated_frame, (int(width/2), int(height/2)))
        cv2.imshow("YOLO11 Tracking", annotated_frame)
        
        out.write(annotated_frame)

        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
