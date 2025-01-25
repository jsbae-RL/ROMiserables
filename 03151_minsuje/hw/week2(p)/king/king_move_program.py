from chess_board import ChessBoard


# 입력 받기
king_pos, stone_pos, n = input().split()
n = int(n)
commands = [input().strip() for _ in range(n)]
# 게임 초기화 및 실행
game = ChessBoard(king_pos, stone_pos, commands)
king_final, stone_final = game.get_positions()

# 결과 출력
print(king_final)
print(stone_final)