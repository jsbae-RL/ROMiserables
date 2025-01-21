# https://www.acmicpc.net/problem/1063

class Chessboard:
    def __init__(self):
        self.king_column, self.king_row = 0, 0
        self.rock_column, self.rock_row = 0, 0


    def king_location(self, king):
        '''
        킹의 위치 입력 (초기값)
        '''
        self.king_column = ord(king[0]) - ord('A')   # 알파벳을 열 좌표로 변환(A=0, B=1, ..., H=7)
        self.king_row = 8 - int(king[1])             # 숫자를 행 좌표로 변호나(1=7, 2=6, ..., 8=0)                   
        
    def rock_location(self, rock):
        '''
        돌의 위치 입력 (초기값)
        '''
        self.rock_column = ord(rock[0]) - ord('A')   # 알파벳을 열 좌표로 변환(A=0, B=1, ..., H=7)
        self.rock_row = 8 - int(rock[1])             # 숫자를 행 좌표로 변호나(1=7, 2=6, ..., 8=0)

    def move_king(self, move):
        '''
        1. 움직이는 횟수 N 만큼 킹의 이동 방향 입력하고
        2. 조건이 맞다면 킹을 이동시킨다
        3. 킹을 이동 시킨 이후 돌과의 충돌을 처리한다
        '''
        d_column, d_row = 0, 0
        updated_king_column, updated_king_row = 0, 0

        if move == "R":                 # 한 칸 오른쪽으로
            d_column = 1
        elif move == "L":               # 한 칸 왼쪽으로
            d_column = -1
        elif move == "B":               # 한 칸 아래로
            d_row = 1
        elif move == "T":               # 한 칸 위로
            d_row = -1
        elif move == "RT":              # 오른쪽 위 대각선으로
            d_column = 1
            d_row = -1
        elif move == "LT":              # 왼쪽 위 대각선으로
            d_column = -1
            d_row = -1 
        elif move == "RB":              # 오른쪽 아래 대각선으로
            d_column = 1
            d_row = 1
        elif move == "LB":              # 왼쪽 아래 대각선으로
            d_column = -1
            d_row = 1

        updated_king_column = self.king_column + d_column   # 킹의 열을 업데이트
        updated_king_row = self.king_row + d_row            # 킹의 행을 업데이트

        if (updated_king_column < 0 or updated_king_column >= 8 or  # 해당 이동을 통해 킹이 8*8크기의 체스판의 범위를 넘어간다면
            updated_king_row < 0 or updated_king_row >= 8):         # 해당 이동을 무시하고 다음 이동을 입력받는다
            return

        self.king_column = updated_king_column                      # 업데이트된 내용을 실제 킹의 위치에 반영시킨다
        self.king_row = updated_king_row

        if (self.king_column == self.rock_column and self.king_row == self.rock_row):   # 킹과 돌이 충돌이 일어난다면
            self.rock_column += d_column                                                # 돌을 킹이 이동한 방향으로 이동시킨다.
            self.rock_row += d_row

    def print_result(self):
        print(chr(self.king_column + ord('A')), str(8 - self.king_row))
        print(chr(self.rock_column + ord('A')), str(8 - self.rock_row))

king, rock, count = input().split()  # 킹의 위치, 돌의 위치, 움직이는 횟수 N 입력하기
count = int(count)
board = Chessboard()
if (len(king) != 2 or king[0] < 'A' or king[0] > 'H' or king[1] < '1' or king[1] > '8' or
    len(rock) != 2 or rock[0] < 'A' or rock[0] > 'H' or rock[1] < '1' or rock[1] > '8' or
    count > 50):
        print("입력 오류: A~H와 1~8 범위로 입력, count는 50을 넘을 수 없습니다.")
        exit(1)
else:
    board.king_location(king)           # 옳게 입력시 초기값이 설정된다
    board.rock_location(rock)

for _ in range(count):                  # 움직이는 횟수 N 만큼 킹의 이동 방향 입력하기
    move = input()
    board.move_king(move)

board.print_result()