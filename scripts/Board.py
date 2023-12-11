from scripts.Constants import *
from scripts.Squares import Square

class Board:

    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0,] for col in range(COLS)]
        self._Create()

    def _Create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        pass