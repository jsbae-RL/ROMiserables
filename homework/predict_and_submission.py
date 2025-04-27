# YOLOv11n use
# 최신 딥러닝, 최적화 반영, ultralytics 최신 아키텍처 백본과 네크구조 개선됨, 소규모객체-헬멧에 적합해보임





from ultralytics import YOLO
import pandas as pd
import os

# 설정
data_dir = "/home/kimseohee/kaggle_competition/data"
test_image_dir = os.path.join(data_dir, "test/images")
model_path = "/home/kimseohee/kaggle_competition/runs/detect/train5/weights/best.pt"
output_csv = "/home/kimseohee/kaggle_competition/submission.csv"

# 테스트 이미지 확인
test_images = [f for f in os.listdir(test_image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
if not test_images:
    raise FileNotFoundError(f"No images found in {test_image_dir}")

# 모델 로드
model = YOLO(model_path)
model.to('cpu')  # CPU 사용

# 예측 결과 저장
submission_data = []
box_id = 0

# 예측
results = model(
    test_image_dir,
    stream=True,
    imgsz=416,  # 학습과 동일
    conf=0.4,  # mAP@0.5 최적화
    iou=0.6,  # NMS
    batch=4,  # CPU 부하 감소
    device='cpu'  # CPU 사용
)

for result in results:
    image_id = os.path.basename(result.path)
    if result.boxes is not None and len(result.boxes):
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            submission_data.append([
                f"sub_{box_id}",
                image_id,
                cls,
                int(x1),
                int(y1),
                int(x2),
                int(y2),
                conf
            ])
            box_id += 1

# CSV 저장
columns = ["id", "image_id", "class", "x1", "y1", "x2", "y2", "confidence"]
df = pd.DataFrame(submission_data, columns=columns)
df.to_csv(output_csv, index=False)
print(f"Saved prediction results to {output_csv}")