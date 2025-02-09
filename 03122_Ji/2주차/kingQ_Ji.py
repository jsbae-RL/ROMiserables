# https://www.acmicpc.net/problem/1063
# 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 
# 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 
# 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 
# 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

# 킹은 다음과 같이 움직일 수 있다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.
# 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

# 출력
# 첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로

move = {
    'R':(1,0),
    'L':(-1,0),
    'B':(0,-1),
    'T':(0,1),
    'RT':(1,1),
    'LT':(-1,1),
    'RB':(1,-1),
    'LB':(-1,-1)
}
chessboard_n2a = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}   # 좌표 계산으로 움직인 후 체스 위치로 변환하기 위한 딕셔너리
chessboard_a2n = {val:key for key, val in chessboard_n2a.items()}           # 초기 위치를 받았을때 좌표로 변환하기 위한 딕셔너리리

class Chessmen:
    '''
    체스말 클래스
    '''
    def __init__(self, initial):                        # 초기 위치(문자열)를 받아서 숫자로 변환 후 리스트에 저장장
        self.now = []
        self.now.append(chessboard_a2n[initial[0]])
        self.now.append(int(initial[1]))
    
    def where(self):                                    # 현재 위치 반환: 숫자 -> 문자자
        self.now_board = chessboard_n2a[self.now[0]] + str(self.now[1])
        return self.now_board
    
    def move(self, moving_cmd):                         # 체스말 이동
        for i in range(2):
            self.now[i] += move[moving_cmd][i]
            if self.now[i] > 8 or self.now[i] < 1:      # 체스판의 범위를 넘으면 False 반환환
                return False
        return True
            
    def move_back(self, moving_cmd):                    # 커맨드 반대로 되돌아가는 함수
        for i in range(2):
            self.now[i] -= move[moving_cmd][i]

first = input('킹의 위치, 돌의 위치, 움직이는 횟수를 입력하시오:').split()      # 한줄에 입력받은 문자열을 나눠서 리스트에 저장장

king = Chessmen(first[0])           # king 객체 초기 위치(문자열) 주며 초기화화
dol = Chessmen(first[1])            # dol 객체 초기 위치(문자열) 주며 초기화화
n = int(first[2])                   # 반복횟수 숫자로 저장장

def move_chessman(cmd):             # 킹 이동 및 돌과 겹치면 돌 이동, 체스판을 넘어가면면 다시 원래 자리로 돌아가게 하는 함수
    king_next = king.move(cmd)      # 킹 이동동
    if king_next == False:          # 킹 이동이 체스판 범위를 넘음
        king.move_back(cmd)            # 킹 움직임 번복                  
    elif king.now == dol.now:         # 킹과 돌의 위치가 같다
        dol_next = dol.move(cmd)    # 돌을 킹이 움직인 방향으로 움직임
        if dol_next == False:       # 돌이 체스판 벗어남
            king.move_back(cmd)     # 킹과 돌 원래 자리로 돌아감
            dol.move_back(cmd)
            return
    
	
for i in range(n):                  # 입력받은 수만큼 킹 이동 함수 반복복
    moving_cmd = input()            # 반복하는 횟수만큼 커맨드 입력받음
    move_chessman(moving_cmd)
    
print(king.where(),dol.where())
