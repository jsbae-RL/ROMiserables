import cv2
from ultralytics import YOLO

# YOLOv11 모델 불러오기
model = YOLO("./yolo11n.pt")

cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Could not open video device")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('./output.avi', fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 불러온 yolov11에 frame을 인자로 넣어 결과를 반환
    # results는 좌표값, 클래스, confidence score등의 결과가 반환
    results = model(frame)

    # 탐지된 결과를 frame에 그리기 위한 xy좌표 출력
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # bounding box의 좌표를 추출
            conf = box.conf[0]  # Confidence score 추출
            cls = int(box.cls[0])  # Class index를 추출
            
            label = f"{model.names[cls]}: {conf:.2f}" # 추출된 Class index와 class 이름을 매칭
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # 추출된 좌표를 가지고 bounding box 표시
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # class를 bounding box 상단에 작성
    
    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == ord('q'):
        print('quit')
        break

cap.release()
out.release()
cv2.destroyAllWindows()