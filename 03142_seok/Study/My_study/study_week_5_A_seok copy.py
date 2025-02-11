from collections import deque

class Puyo:
    def __init__(self):
        self.row, self.column = 12, 6
        self.colors = {"R": 1, "G": 2, "B": 3, "P": 4, "Y": 5}
        self.board = []
        self.dx = [1, -1, 0, 0]  # 상하좌우 이동
        self.dy = [0, 0, 1, -1]

    def insert_board(self):
        self.board = [list(input().strip()) for _ in range(12)]

    def bfs(self, x, y, color, visited):
        queue = deque([(x, y)])
        visited[x][y] = True
        blocks = [(x, y)]  # 연결된 블록 좌표 저장
        
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + self.dx[i], cy + self.dy[i]
                if 0 <= nx < self.row and 0 <= ny < self.column:
                    if not visited[nx][ny] and self.board[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        blocks.append((nx, ny))
        
        return blocks
    
    def erase_blocks(self, blocks):
        for x, y in blocks:
            self.board[x][y] = '.'  # 제거된 블록은 '.'으로 변경

    def gravity(self):
        for col in range(self.column):
            temp_col = [self.board[row][col] for row in range(self.row) if self.board[row][col] != '.']
            temp_col = ['.'] * (self.row - len(temp_col)) + temp_col  # '.'을 위로 채움
            for row in range(self.row):
                self.board[row][col] = temp_col[row]
    
    def is_not_erase(self):
        visited = [[False] * self.column for _ in range(self.row)]
        found = False
        
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j] != '.' and not visited[i][j]:
                    blocks = self.bfs(i, j, self.board[i][j], visited)
                    if len(blocks) >= 4:  # 4개 이상 연결된 경우
                        self.erase_blocks(blocks)
                        found = True
        
        return found

game = Puyo()
game.insert_board()
cnt = 0

while True:
    if not game.is_not_erase():  # 더 이상 터질 뿌요가 없으면 종료
        break
    game.gravity()
    cnt += 1

print(cnt)
