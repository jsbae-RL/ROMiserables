"""
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
x는 세로 방향으로 센다(행), y는 가로 방향으로 센다(열)

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

"""

from collections import deque

class Puyo:
    
    def __init__(self):
        self.row, self.column = 12, 6
        self.delta_x = [1, -1, 0, 0] # 상, 하, 좌, 우
        self.delta_y = [0, 0, -1, 1]

    def insert_puyo_in_board(self, board_data):

        self.board = [list(line.strip()) for line in board_data.strip().splitlines()]


    def bfs(self, x, y, color, visited):
        queue = deque([(x, y)])
        visited[x][y] = True     # 현재 위치 방문 처리 
        blocks = [(x, y)]        # 연결된 블록 좌표 저장

        while queue:
            current_x, current_y = queue.popleft()
            for i in range(4):
                next_x = current_x + self.delta_x[i]
                next_y = current_y + self.delta_y[i]
                if 0 <= next_x < self.row and 0 <= next_y < self.column: # 보드 안에 있으며
                    if not visited[next_x][next_y]:                      # 아직 방문하지 않았고
                        if self.board[next_x][next_y] == color:          # 색상이 같다면
                            visited[next_x][next_y] = True               # 방문처리 하고
                            queue.append((next_x, next_y))
                            blocks.append((next_x, next_y))
        return blocks
    
    def change_to_dot(self, blocks):
        for x, y in blocks:
            self.board[x][y] = '.'

    def gravity(self):
        for col in range(self.column):
            for row in range(self.row -1, -1, -1):       # 아래에서 위로 탐색
                if self.board[row][col] == '.':         # 빈칸인 '.'을 발견하면
                    for go_up in range(row - 1, -1, -1): # 그곳의 위쪽에서 블록을 찾은 후 스왑합니다.
                        if self.board[go_up][col] != '.':
                            self.board[row][col], self.board[go_up][col] = self.board[go_up][col], self.board[row][col]
                            break   # 스왑 후 종료
    
    def explode_blocks(self):
        visited = [[False] * self.column for _ in range(self.row)] # 6*12 크기의 False 들을 가지고
        found = False

        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j] != '.':         # 빈칸인 '.'이 아니면서
                    if not visited[i][j]:           # 아직 방문하지 않았다면 
                        blocks = self.bfs(i, j, self.board[i][j], visited)
                        if len(blocks) >= 4:
                            self.change_to_dot(blocks)
                            found = True
        return found
    
if __name__ == "__main__":

    board_data =    """
                    ......
                    ......
                    ......
                    ......
                    ......
                    ......
                    ......
                    ......
                    .Y....
                    .YG...
                    RRYG..
                    RRYGG.
                    """

    game = Puyo()
    game.insert_puyo_in_board(board_data)
    cnt = 0

    while True:
        if not game.explode_blocks(): # 더 이상 터질 뿌요가 없으면 종료
            break
        game.gravity()
        cnt += 1
    
    print(cnt)