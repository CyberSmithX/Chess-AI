import pygame
from scripts.Constants import *
from scripts.Themes import Backgrounds
from scripts.Board import Board

class Game:
    def __init__(self) -> None:
        self.board = Board()

    def load_background(self, surface) -> None:
        bg = Backgrounds()
        bg.Default(surface)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # pieces
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2 , row * SQUARE_SIZE + SQUARE_SIZE // 2

                    piece.texture_rect = img.get_rect(center=img_center)

                    surface.blit(img, piece.texture_rect)