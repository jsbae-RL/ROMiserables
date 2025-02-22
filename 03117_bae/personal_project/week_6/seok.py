def solution(board):
    answer = 1

    board_value = [i for li in board for i in li]
    O_count = board_value.count('O')
    X_count = board_value.count('X') 

    # 선공은 O, 빈값도 가능(X만 존재하면 안된다)
    if (set(board_value) == {"X"}) or (set(board_value)=={".", "X"}):
        answer = 0

    # O 의 개수는 X와 동일하거나 1개 많아야한다.
    temp_value = O_count - X_count
    if temp_value not in [0,1]:
        answer = 0

    # O or X가 규칙에 맞는 3개면 게임이 정상적으로 종료 되어야 한다.
    if game_over(board, "O"):
        if temp_value != 1:
            answer = 0
        else:
            if game_over(board, "X"):
                answer = 0
    elif game_over(board, "X"):
        if temp_value != 0:
            answer = 0
    else:
        ("Not over")
    return answer

# O의 승리여부를 먼저 탐색해야한다.(player 변수 추가)
def game_over(board, player):
    for i in range(3):
        # 가로 확인
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # 세로 확인
        elif board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False