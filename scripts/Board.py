from scripts.Constants import *
from scripts.Squares import Square
from scripts.Piece import *

class Board:

    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0,] for col in range(COLS)]
        self._Create()
        self._add_piece("black")
        self._add_piece("white")

    def _Create(self):
        for row in range(ROWS):
            for col in range(COLS): 
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        if color == "white":
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        # Adding Pawns to the Board
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Adding Knights to the Board
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        # Adding Bishop to the Board
        self.squares[row_other][2] = Square(row_other, 1, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 6, Bishop(color))

        # Adding Rook to the Board
        self.squares[row_other][0] = Square(row_other, 1, Rook(color))
        self.squares[row_other][7] = Square(row_other, 6, Rook(color))

        # Adding Queen to the Board
        self.squares[row_other][3] = Square(row_other, 1, Queen(color))

        # Adding King to the Board
        self.squares[row_other][4] = Square(row_other, 1, King(color))