class ChessBoard:
    def __init__(self, king_pos, stone_pos, commands):
        ''' 
        초기화 함수
        - king_pos: 왕의 초기 위치
        - stone_pos: 돌의 초기 위치
        - commands: 명령리스트트
        '''
        # 명령어 좌표 이동동
        self.directions = {         
            'R': (0, 1),    # 오른쪽 (y축 증가)
            'L': (0, -1),   # 왼쪽 (y축 감소)
            'B': (1, 0),    # 아래쪽 (x축 증가)
            'T': (-1, 0),   # 위쪽 (x축 감소)
            'RT': (-1, 1),  # 오른쪽 위 대각선
            'LT': (-1, -1), # 왼쪽 위 대각선
            'RB': (1, 1),   # 오른쪽 아래 대각선
            'LB': (1, -1)   # 왼쪽 아래 대각선
        }
        
        # 초기 위치 정보 변환하여 저장 및 명령어 저장
        self.king = self.pos_to_index(king_pos)
        self.stone = self.pos_to_index(stone_pos)
        self.commands = commands
        # 초기화 후 내부에서 바로 결과 내는게 더 맞다고 생각들어서함.
        self.move()
        
    def pos_to_index(self, pos):
        ''' 
        문자열 위치를 좌표 평면으로 변환
        '''
        col, row = pos[0], pos[1]  # pos에서 열과 행을 분리
        # 행은 1부터 시작되므로, 배열에서는 row - 1로 변환
        # 열은 'A'의 ASCII 값에서 빼서 0부터 시작하는 숫자로 변환
        return (int(row) - 1, ord(col) - ord('A'))
    
    def index_to_pos(self, index):
        ''' 
        좌표 평면위치를 문자열 위치로 변환
        '''
        row, col = index  # 인덱스에서 행과 열을 분리
        # 행은 1부터 시작되고, 배열은 0에서 시작 됨으로row+1
        # 열은 'A'의 ASCII 값에서 빼서 0부터 했으니 반대로 'A'를 더해서  ASCII로 변환환
        return f"{chr(col + ord('A'))}{row + 1}"

    def is_within_bounds(self, pos):
        ''' 
        주어진 좌표가 체스판의 범위 내에 있는지 확인하는 함수
        '''
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    def move(self):
        ''' 
        저장된 명령어들을 하나씩 처리리
        명령에 의해 좌표를 이동 하되 범위내에 있는지 확인하며 벗어났으면 무시하고 넘김김
        '''
        for command in self.commands:
            move = self.directions[command]
            # 명령에 의한 king의 새로운 좌표 위치 저장
            new_king = (self.king[0] + move[0], self.king[1] + move[1])
            # king이 좌표를 벗어 나면 
            if not self.is_within_bounds(new_king):
                continue  # 다음명령으로 감
            # 새로운 king의 좌표가 stone의 좌표와 같으면
            if new_king == self.stone:
                # stone은 king의 이동과 같은 방향으로 같은 크기로 이동
                new_stone = (self.stone[0] + move[0], self.stone[1] + move[1])
                # stone이 좌표를 벗어 났으면
                if not self.is_within_bounds(new_stone):
                    continue  # 다음명령으로감
                # stone의 위치 업데이트
                self.stone = new_stone
            # king의 위치 업데이트
            self.king = new_king

    def get_positions(self):
        ''' 
        문자열 위치 좌표로 king과 stone 위치 반환. 
        '''
        # 왕과 돌의 좌표를 문자로 변환하여 반환
        return self.index_to_pos(self.king), self.index_to_pos(self.stone)