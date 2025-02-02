import cv2

cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Could not open video device")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 저장하려는 영상의 코덱 설정
# 영상 코덱이란?
    #  영상신호를 디지털 신호로 변환하여 컴퓨터가 읽을 수 있게 하고,
    #  다시 모니터에 원래의 영상신호로 변환하여 사용자가 알 수 있게 재생 시켜주는 소프트웨어
# 이러한, 코덱은 저장하려는 영상의 확장자에 따라 인자가 달라진다.
# mp4v = .mp4 or .mov /  DIVX or XVID = .avi 등  
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 영상 클래스를 객체화
# 인자
    # 1. 영상을 저장하기 위한 경로
    # 2. 영상 코덱
    # 3. fps
    # 4. 해상도 높이(int), 너비(int)
out = cv2.VideoWriter('./output.avi', fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # frame을 인자로 하여 영상 저장
    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == ord('q'):
        print('quit')
        break

cap.release()
# 메모리 정리 : 영상 저장 끝내기
out.release()
cv2.destroyAllWindows()