import numpy as np
from game.core.config import *
from game.core.pieces import Piece

class Grid:
    def __init__(self):
        self.rows = grid_rows
        self.cols = grid_cols
        self.block_size = block_size
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self.game_zone_width = game_zone_width
        self.game_zone_height = game_zone_height

    def is_valid_position(self, piece: Piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col]:
                    new_row, new_col = piece.row + row, piece.col + col
                    if new_row >= self.rows or new_col >= self.cols or new_col < 0:
                        return False
                    if self.grid[new_row, new_col]:
                        return False
        return True

    def add_piece(self, piece: Piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col]:
                    self.grid[piece.row + row, piece.col + col] = piece.color

    def clear_lines(self):
        full_rows = [row for row in range(self.rows) if all(self.grid[row])]
        for row in full_rows:
            self.grid = np.delete(self.grid, row, axis=0)
            self.grid = np.vstack([np.zeros((1, self.cols), dtype=int), self.grid])
        return len(full_rows)

    def check_game_over(self):
        return any(self.grid[0])
