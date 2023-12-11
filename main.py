import pygame
import sys
from scripts.Constants import *
from scripts.Game import Game


class Main:

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chess AI - Signature Developer")

    def mainloop(self) -> None:

        screen = self.screen
        game = Game()

        while True:
            screen.fill(BLACK)
            game.load_background(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    game = Main()
    game.mainloop()
