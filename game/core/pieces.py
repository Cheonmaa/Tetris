import random
import numpy as np
from game.core.config import *

class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.rotation = 0
        self.row = 0
        self.col = grid_cols // 2 - len(self.shape[0]) // 2

    def rotate(self):
        new_rotation = (self.rotation + 1) % len(self.shape)
        self.rotation = new_rotation

    def get_rotated_shape(self):
        return self.shape[self.rotation]
    
    def move_down(self, grid):
        self.row += 1
        if not grid.is_valid_position(self):
            self.row -= 1
            return False
        return True
    
    def move_left(self, grid):
        self.col -= 1
        if not grid.is_valid_position(self):
            self.col += 1
    
    def move_right(self, grid):
        self.col += 1
        if not grid.is_valid_position(self):
            self.col -= 1