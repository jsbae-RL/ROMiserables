import re
class Chessboard:
    def __init__(self):
        '''
        00 01 02 03 04 05 06 07     A8 B8 C8 D8 E8 F8 G8 H8
        10 11 12 13 14 15 16 17     A7 B7 C7 D7 E7 F7 G7 H7
        20 21 22 23 24 25 26 27     A6 B6 C6 D6 E6 F6 G6 H6
        30 31 32 33 34 35 36 37     A5 B5 C5 D5 E5 F5 G5 H5
        40 41 42 43 44 45 46 47  -> A4 B4 C4 D4 E4 F4 G4 H4
        50 51 52 53 54 55 56 57     A3 B3 C3 D3 E3 F3 G3 H3
        60 61 62 63 64 65 66 67     A2 B2 C2 D2 E2 F2 G2 H2
        70 71 72 73 74 75 76 77     A1 B1 C1 D1 E1 F1 G1 H1
        '''
        self.king_column, self.king_row = 0, 0
        self.rock_column, self.rock_row = 0, 0

    def king_location(self, king):
        '''
        킹의 위치 입력 (초기값)
        '''
        self.king_column = ord(king[0]) - ord('A')   # 알파벳을 열 좌표로 변환(A=0, B=1, ..., H=7)
        self.king_row = 8 - int(king[1])             # 숫자를 행 좌표로 변환(1=7, 2=6, ..., 8=0)                   

    def rock_location(self, rock):    
        '''
        돌의 위치 입력 (초기값)
        '''
        self.rock_column = ord(rock[0]) - ord('A')   # 알파벳을 열 좌표로 변환(A=0, B=1, ..., H=7)
        self.rock_row = 8 - int(rock[1])             # 숫자를 행 좌표로 변환(1=7, 2=6, ..., 8=0)

    def move_king(self, move):
        '''
        1. 움직이는 횟수 N 만큼 킹의 이동 방향 입력하고
        2. 조건이 맞다면 킹을 이동시킨다
        3. 킹을 이동 시킨 이후 돌과의 충돌을 처리한다
        '''
        updated_king_column, updated_king_row = 0, 0
        updated_rock_column, updated_rock_row = 0, 0

        dic = {"R":[0, 1],      # 한 칸 오른쪽으로
               "L":[0, -1],     # 한 칸 왼쪽으로
               "B":[1, 0],      # 한 칸 아래로
               "T":[-1, 0],     # 한 칸 위로
               "RT":[-1, 1],    # 오른쪽 위 대각선으로
               "LT":[-1, -1],   # 왼쪽 위 대각선으로
               "RB":[1, 1],     # 오른쪽 아래 대각선으로
               "LB":[1, -1]}    # 왼쪽 아래 대각선으로
        
        d_row, d_column = dic[move]  # 이동 방향 결정

        updated_king_column = self.king_column + d_column   # 킹의 열을 업데이트
        updated_king_row = self.king_row + d_row            # 킹의 행을 업데이트
        '''
        킹의 위치 업데이트 시도
        '''
        
        if not (0 <= updated_king_column < 8 and 0 <= updated_king_row < 8):    # 해당 이동을 통해 킹이 8*8크기의 체스판의 범위를 넘어간다면
            return                                                              # 해당 이동을 무시하고 다음 이동을 입력받는다
        '''
        킹이 체스판 범위를 넘어가면 무시
        '''

        if (updated_king_column == self.rock_column and updated_king_row == self.rock_row):   # 킹과 돌이 충돌이 일어난다면
            updated_rock_column = self.rock_column + d_column                                 # 돌을 킹이 이동한 방향으로 이동시킨다.
            updated_rock_row = self.rock_row + d_row
            '''
            킹과 돌 충돌 여부 검사 및 돌의 위치 업데이트 시도
            '''

            if not (0 <= updated_rock_column < 8 and 0 <= updated_rock_row < 8):    # 해당 이동을 통해 돌이 8*8크기의 체스판의 범위를 넘어간다면
                return                                                              # 돌이 이동할 수 없으므로 킹의 이동을 취소
            '''
            돌이 체스판 범위를 넘어가면 킹의 이동 취소
            '''

            self.rock_column = updated_rock_column  # 돌의 열 좌표 업데이트
            self.rock_row = updated_rock_row        # 돌의 행 좌표 업데이트

        self.king_column = updated_king_column  # 킹의 열 좌표 업데이트
        self.king_row = updated_king_row        # 킹의 행 좌표 업데이트
        '''
        킹과 돌의 위치 업데이트
        '''

    def print_result(self):
        print_king_column = chr(self.king_column + ord('A'))    # 열 좌표를 알파벳으로 변환(65=A, 66=B, ..., 72=H)
        print_king_row = 8 - self.king_row                      # 행 좌표를 숫자로 변환(7=1, 6=2, ..., 0=8)
        print_rock_column = chr(self.rock_column + ord('A'))    # 열 좌표를 알파벳으로 변환(65=A, 66=B, ..., 72=H)
        print_rock_row = 8 - self.rock_row                      # 행 좌표를 숫자로 변환(7=1, 6=2, ..., 0=8)
        print(f"{print_king_column}{print_king_row}") 
        print(f"{print_rock_column}{print_rock_row}")

range_of_king_rock_count = re.compile(r"[A-H][1-8]\s[A-H][1-8]\s([1-9]|[1-4][0-9]|50)")   # 유효 입력 예시 : A1 A2 20
king_rock_count = input()
                    
if range_of_king_rock_count.match(king_rock_count):
    king = king_rock_count[0:2]
    rock = king_rock_count[3:5]
    count = king_rock_count[6:]
else:
    print("잘못된 입력입니다.")
    exit(0)

board = Chessboard()
board.king_location(king)  # 킹의 위치 설정
board.rock_location(rock)  # 돌의 위치 설정

for _ in range(int(count)):                  # 움직이는 횟수 N 만큼 킹의 이동 방향 입력하기
    move = input()
    board.move_king(move)

board.print_result()
