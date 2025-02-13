'''
만약 bytetrack설치에 성공한다면, 사용가능
'''

import cv2
from ultralytics import YOLO
from bytetrack import BYTETracker   # bytetrack 설치후 사용 가능
import torch

# YOLOv11 모델 불러오기
model = YOLO("./yolo11n.pt")

# ByteTrack 초기화
tracker = BYTETracker()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open video device")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./output.avi', fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv11 탐지 수행
    results = model(frame)
    detections = []  # 탐지된 객체 리스트

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 바운딩 박스 좌표
            conf = float(box.conf[0])  # 신뢰도 점수
            cls = int(box.cls[0])  # 클래스 ID
            detections.append([x1, y1, x2, y2, conf, cls])

    # Bytetrack을 활용하여 객체 추적
    tracks = tracker.update(torch.tensor(detections)) # torch를 써도 되는지는 확인 필요

    for track in tracks:
        x1, y1, x2, y2, track_id, cls = map(int, track[:6])
        label = f"ID {track_id}: {model.names[cls]}"
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # 바운딩 박스 표시
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # ID 표시
    
    out.write(frame)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(10) == ord('q'):
        print('quit')
        break

cap.release()
out.release()
cv2.destroyAllWindows()
