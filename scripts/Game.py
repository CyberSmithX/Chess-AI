import pygame
from scripts.Constants import *
from scripts.Themes import Backgrounds

class Game:
    def __init__(self) -> None:
        pass

    def load_background(self, surface) -> None:
        bg = Backgrounds()
        bg.Default(surface)