import numpy as np
# 보드 를 넘파이로 하면 쉽긴 하겠다 생각함.
# board = np.array([
#     ['.','.','.'],
#     ['.','.','.'],
#     ['.','.','.']   
# ])
'''
조건 1. "." 빈칸, "O","X"만 올수 있다.
조건 2. "O"가 선공
조건 3. 승리 후 게임 진행 불가능
'''
class TicTacToeValidator:
    def __init__(self, board):
        self.set_board(board)
    
    def set_board(self, board):
        self.board = np.array([[c for c in row] for row in board])
    
    # "O"가 "X"의 개수와 같거나 1개 더 많으면 정상 아니면 비정상
    def validate_counts(self):
        o_count = np.count_nonzero(self.board == 'O')
        x_count = np.count_nonzero(self.board == 'X')
        return o_count == x_count or o_count == x_count + 1
    
    # 승리자 확인
    def check_winner(self, player):
        # 행과 열 검사
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        # 대각선 검사 np.all(np.diag(self.board) 대각선이 X의 값이니? np.fliplr(self.board)대칭시킴 
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False
    
    #조건을 충족하는지 확인
    def is_valid(self):
        if not self.validate_counts():
            return 0
        
        o_wins = self.check_winner('O')
        x_wins = self.check_winner('X')
        
        if o_wins and x_wins:
            return 0  # 둘 다 승리 상태면 잘못된 게임 상태
        if o_wins and np.count_nonzero(self.board == 'O') != np.count_nonzero(self.board == 'X') + 1:
            return 0  # O가 이겼는데 개수 조건이 맞지 않음(O가 이기면 O가 X보다 1개 더 많이 되어있음 만약 X가 미리 이겼으면 이전 조건에 이미 클리어)
        if x_wins and np.count_nonzero(self.board == 'O') != np.count_nonzero(self.board == 'X'):
            return 0  # X가 이겼는데 개수 조건이 맞지 않음(X가 이기면 X가 O랑 개수가 같음 만약 O도 이긴건 위의 조건에 이미 클리어)
        
        return 1  # 유효한 게임 상태

# 테스트 예시
board = ["O.X", ".O.", "..X"]
validator = TicTacToeValidator(board)
print(validator.is_valid())

board = ["OOO", "...", "XXX"]
validator = TicTacToeValidator(board)
print(validator.is_valid())

board = ["...", ".X.", "..."]
validator = TicTacToeValidator(board)
print(validator.is_valid())

board = ["...", "...", "..."]
validator = TicTacToeValidator(board)
print(validator.is_valid())