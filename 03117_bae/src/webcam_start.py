# opencv 모듈 호출
import cv2

# id가 0번인 카메라에서 비디오가 반환
cap = cv2.VideoCapture(0)

# 카메라가 연결이 되어 있는지 안되어 있는지 확인
# 만약, 웹캠이 분명 연결되어있는데, 하단에 문구가 뜬다면 접촉불량일 수 있다.
if not (cap.isOpened()):
    print("Could not open video device")

# 카메라의 해상도를 지정
# 너비(가로) 640, 높이(세로) 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:
    # 연결된 카메라를 frame으로 읽음
    # ret는 frame이 생성되면 True 또는 아니면 False를 반환
    # _, frame = cap.read()라고 되어있는 것들도 있다.
    ret, frame = cap.read()

    # ret == False면 break
    if not ret:
        break
    
    # 읽어낸 frame을 출력
    cv2.imshow('frame', frame)

    # while문을 벗어날 이벤트를 생성
    # 키보드의 q를 입력할시 quit를 터미널에 출력하고 반복문을 break
    if cv2.waitKey(10) == ord('q'):
        print('quit')
        break

# 최종 메모리 정리
cap.release()
cv2.destroyAllWindows()