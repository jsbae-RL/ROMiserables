class Chessboard:
    DIRECTIONS = {
        "R": (1, 0), "L": (-1, 0), "T": (0, -1), "B": (0, 1),
        "RT": (1, -1), "LT": (-1, -1), "RB": (1, 1), "LB": (-1, 1)
    }

    def __init__(self, king, rock):
        # Initialize king and rock positions
        self.king_column, self.king_row = self.to_coordinates(king)
        self.rock_column, self.rock_row = self.to_coordinates(rock)

    def to_coordinates(self, position):
        """Convert chess notation (e.g., 'A1') to (column, row) coordinates."""
        column = ord(position[0]) - ord('A')  # A=0, B=1, ..., H=7
        row = 8 - int(position[1])           # 8=0, 7=1, ..., 1=7
        return column, row

    def to_chess_notation(self, column, row):
        """Convert (column, row) coordinates back to chess notation."""
        return f"{chr(column + ord('A'))}{8 - row}"

    def is_within_bounds(self, column, row):
        """Check if the position is within the chessboard boundaries."""
        return 0 <= column < 8 and 0 <= row < 8

    def move_king(self, move):
        """Move the king in the given direction and adjust the rock if necessary."""
        if move not in self.DIRECTIONS:
            return  # Ignore invalid directions

        d_column, d_row = self.DIRECTIONS[move]
        new_king_column = self.king_column + d_column
        new_king_row = self.king_row + d_row

        # Check if the king's new position is within bounds
        if not self.is_within_bounds(new_king_column, new_king_row):
            return

        # Update king's position
        self.king_column, self.king_row = new_king_column, new_king_row

        # If the king and rock collide, move the rock
        if (self.king_column, self.king_row) == (self.rock_column, self.rock_row):
            new_rock_column = self.rock_column + d_column
            new_rock_row = self.rock_row + d_row

            # Only move the rock if the new position is within bounds
            if self.is_within_bounds(new_rock_column, new_rock_row):
                self.rock_column, self.rock_row = new_rock_column, new_rock_row
            else:
                # Revert king's move if rock can't move
                self.king_column -= d_column
                self.king_row -= d_row

    def print_result(self):
        """Print the final positions of the king and the rock."""
        print(self.to_chess_notation(self.king_column, self.king_row))
        print(self.to_chess_notation(self.rock_column, self.rock_row))


# Main execution
def main():
    king, rock, count = input().split()
    count = int(count)

    # Validate inputs
    if not (len(king) == 2 and len(rock) == 2 and 'A' <= king[0] <= 'H' and '1' <= king[1] <= '8' and
            'A' <= rock[0] <= 'H' and '1' <= rock[1] <= '8' and 1 <= count <= 50):
        print("입력 오류: A~H와 1~8 범위로 입력, count는 50을 넘을 수 없습니다.")
        return

    # Initialize the chessboard
    board = Chessboard(king, rock)

    # Process each move
    for _ in range(count):
        move = input()
        board.move_king(move)

    # Output the results
    board.print_result()


if __name__ == "__main__":
    main()