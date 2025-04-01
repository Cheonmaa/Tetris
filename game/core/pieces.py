import random
from game.core.config import *

class Piece:
    def __init__(self, x, y , shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choices(COLORS)
        self.rotation = 0

    def new_pieces(self):
        shape = random.choices(SHAPES)
        return shape