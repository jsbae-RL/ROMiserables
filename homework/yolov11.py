from ultralytics import YOLO

# 모델 로드
model = YOLO("yolov11n.pt")

# 학습 설정
model.train(
    data="/home/kimseohee/kaggle_competition/data/custom_data.yaml",  # YAML 경로
    epochs=50,  # CPU 속도 고려, 데이터셋 크기에 따라 조정 (20~50)
    imgsz=640,  # CPU 부하 감소 (원래 640)
    batch=4,  # CPU 메모리 고려
    device='cpu',  # CPU 사용
    patience=5,  # 조기 종료(5 epoch no better)
    augment=True,  # 데이터 증강
    project="/home/kimseohee/kaggle_competition/runs/detect",
    name="train",
    iou=0.5,  # mAP@0.5
    cos_lr=True
)

# 검증
model.val(data="/home/kimseohee/kaggle_competition/data/custom_data.yaml", imgsz=640, iou=0.5, device='cpu')

# 경로 설정을 명확히 하고, mAP@0.5 최적화를 반영