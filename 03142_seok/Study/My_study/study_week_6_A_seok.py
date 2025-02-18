'''
불가능한 상황을 만나면 0을 리턴하도록 만들어야 합니다.
먼저 불가능한 상황을 정리합니다.

1. 불가능한 상황

    가. o가 선공이니 x가 o보다 많아 질 수 없습니다. (보드에서 o와 x의 개수를 세는 코드가 필요합니다.)

        
    나. o가 x보다 2개 이상 많아 질 수 없습니다.

    
    다. o와 x가 둘다 승리 할 수 없습니다. (승리를 검사하는 코드가 필요합니다.)
    
        
    라. o가 승리했는데 x가 o보다 많아 질 수 없습니다.


    마. x가 승리했는데 o가 x보다 많아 질 수 없습니다.


    

2. 승리 검사

    - 가로일 경우

    ooo <- (0,0) (0,1) (0,2)
    ...
    ...

    ...
    ooo <- (1,0) (1,1) (1,2)
    ...

    ...
    ...
    ooo <- (2,0) (2,1) (2,2)

    

    - 세로일 경우

    o.. <- (0,0)
    o.. <- (1,0)
    o.. <- (2,0)

    .o. <- (0,1)
    .o. <- (1,1)
    .o. <- (2,1)

    ..o <- (0,2)
    ..o <- (1,2)
    ..o <- (2,2)

    

    - 대각일 경우

    o.. <- (0,0)
    .o. <- (1,1)
    ..o <- (2,2)

    ..o <- (0,2)
    .o. <- (1,1)
    o.. <- (2,0)


'''


def solution(board):
    def check_winner(player):
        win_cases = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # 가로
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # 세로
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # 대각선
        ]
        for case in win_cases:
            win = True
            for x, y in case:
                if board[x][y] != player:
                    win = False
                    break
            if win:
                return True
        
        return False
    
    o_count = 0
    x_count = 0

    for row in board:
        o_count += row.count('o')
        x_count += row.count('x')
    
    if x_count > o_count or o_count > x_count + 1:
        return 0  # X가 O보다 많거나, O가 X보다 2개 이상 많으면 불가능한 상태
    
    o_wins = check_winner('O')  # 승리시 True, 아닐시 False 반환
    x_wins = check_winner('X')  # 승리시 True, 아닐시 False 반환
    
    if o_wins and x_wins:
        return 0  # 둘 다 승리하는 경우는 불가능한 상태
    if o_wins and o_count == x_count:
        return 0  # O가 이겼는데 개수가 같다면 불가능한 상태
    if x_wins and o_count > x_count:
        return 0  # X가 이겼는데 O가 더 많다면 불가능한 상태
    
    return 1

board = ["O.X", ".O.", "..X"]
print(solution(board))
