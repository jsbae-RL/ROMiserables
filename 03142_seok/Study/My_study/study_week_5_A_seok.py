'''
1. 필요한 함수 분석

가. 뿌요가 4개이상 연결 되어있나 확인하는 함수 
    
 - 그래프 탐색을 통해 해결합니다. (DFS or BFS)


나. 1에서 뿌요가 지워지면 중력을 적용하는 함수 
    
 - for문을 통해 맨 밑에 빈칸이 있다면 swap 합니다.


다. 몇 연쇄인지 카운트 해주는 함수 
    
 - count += 1



2. 보드판 구현

x \ y ================= 
0  | [0, 1, 2, 3, 4, 5]
1  | [0, 1, 2, 3, 4, 5]
2  | [0, 1, 2, 3, 4, 5]
3  | [0, 1, 2, 3, 4, 5]
.            .
.            .
.            .
11 | [0, 1, 2, 3, 4, 5]
========================
x는 세로(행), y는 가로(열)

dx = [1, -1, 0, 0]  # 상, 하, 좌, 우 
dy = [0, 0, -1, 1]



3. 뿌요뿌요 시뮬레이션 ('0'은 폭발을 의미합니다.)

......               ......               ......               ......               ......               ......               ......  
......               ......               ......               ......               ......               ......               ......  
......               ......               ......               ......               ......               ......               ......  
......               ......               ......               ......               ......               ......               ......  
......               ......               ......               ......               ......               ......               ......  
......               ......               ......               ......               ......               ......               ......  
......       →       ......       →       ......       →       ......       →       ......       →       ......       →       ......  
......               ......               ......               ......               ......               ......               ......  
.Y....               .Y....               ......               ......               ......               ......               ......  
.YG...               .YG...               ..G...               ..G...               ......               ......               ......  
RRYG..               00YG..               .YYG..               .00G..               ...G..               ...0..               ......  
RRYGG.               00YGG.               .YYGG.               .00GG.               ..GGG.               ..000.               ......  
                                                                                                                                    
count=0                                   count=1                                   count=2                                   count=3 



4. BFS 탐색을 이용한 폭발


'''
from collections import deque

class Puyo:
    
    def __init__(self):
        self.row, self.column = 12, 6
        self.colors = {"R":1, "G":2, "B":3, "P":4, "Y":5}
        self.delta_x = [1, -1, 0, 0] # 상, 하, 좌, 우
        self.delta_y = [0, 0, -1, 1]

    def insert_puyo_in_board(self):
        self.board = [list(input().strip()) for _ in range(12)]

    def bfs(self, x, y, color, visited):
        queue = deque([(x, y)])
        visited[x][y] = True     # 현재 위치 방문 처리 
        blocks = [(x, y)]        # 연결된 블록 좌표 저장

        while queue:
            current_x, current_y = queue.popleft
            for i in range(4):
                next_x = current_x + self.delta_x[i]
                next_y = current_y + self.delta_y[i]
                if 0 <= next_x < self.row and 0 <= next_y < self.column: # 보드 안에 있으며
                    if not visited[next_x][next_y]:                      # 방문하지 않았고
                        if self.board[next_x][next_y] == color:          # 색상이 같다면
                            visited[next_x][next_y] = True



    def gravity(self):
        pass

    def is_clear(self):
        pass

if __name__ == "__main__":
    game = Puyo()
    game.insert_puyo_in_board()
    cnt = 0

while True:
    if game.is_clear: # 더 이상 터질 뿌요가 없으면 종료
        break
    game.gravity()
    cnt += 1
    
print(cnt)