import cv2
class WebCamSelecter():
    def __init__(self):
        self.cam = None
        self.selected_cam = None
        self.cam_list = []
        self.cam_name = {}
        self.find_cam_list()

    # 카메라를 찾을때 window 11에서만 그럴진 모르겠지만 장치가 한번 이상 인식되면 계속 남아서 연결할수 있게 뜨는데 실제로 연결 안되있으면 error를 반환하긴함
    # 지금 이컴퓨터에 전에 다른 웹캠을 연결 한적있는데 그게 1,2번으로 잡혀 있고, 연결되어있지 않아서 error가 뜸 동작은 함함
    def find_cam_list(self):
        index = 0           # 웹카메라는 노트북의 경우 0번이 노트북 카메라고 나머지가 1~n의 번호로 불러올수있음
        f_cam_list = []
        while(True):
            self.cam = cv2.VideoCapture(index)
            ret, frame = self.cam.read()        # ret은 카메라 상태가 동작가능하면true, 불가능하면 false 프래임은 현재 프레임을 받아옴
            if(not ret):                
                break       # 더 이상 읽어올 카메라 없음.
            self.cam_list.append(index) # 캠의 번호만 저장하는게 프로그램에 덜무리감감
            self.cam.release()      # 카메라 메모리 해제 cam에는 더이상 카메라 정보를 받지 않음
            self.cam_name[index] = ' '
            index +=1

    def select_cam(self,cam_num=0):
        self.selected_cam = self.cam_list[cam_num]

    def name_set(self,cam_num:int, name:str):
        if len(name) <2:
            raise Exception("카메라 이름의 문자는 길이가 1보다 커야합니다.")
        if name in self.cam_name.values():
            raise Exception(f"이미 '{name}'라는 카메라 이름이 존재합니다.")
        self.cam_name[cam_num] = name

    def rename(self,last_name,new_name):
        if len(new_name) <2:
            raise Exception("카메라 이름의 문자는 길이가 1보다 커야합니다.")
        if new_name in self.cam_name.values():
            raise Exception(f"이미 '{new_name}'라는 이름이 존재합니다.")
        for index, name in self.cam_name.items():
            if(last_name==name):
                self.cam_name[index] = new_name
    
    def name2index(self,name:str):
        for index, cam_name in self.cam_name.items():
            if cam_name==name:
                return int(index)
        

# webcam = WebCamSelecter()
# webcam.find_cam_list()
# print(webcam.cam_name)
# webcam.name_set(0,"노트북카메라")
# webcam.name_set(1,"엘가토 웹캠")
# webcam.name_set(2,"모르겠음 웹캠")
# print(webcam.cam_name)
# print(webcam.name2index("엘가토 웹캠"))
