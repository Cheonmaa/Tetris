from game.core.pieces import *

class Grid:
    def __init__(self, rows, cols, block_size):
        self.rows = rows
        self.cols = cols
        self.block_size = block_size
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.game_zone_width = block_size * rows
        self.game_zone_height = block_size * cols

    def is_valid_position(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col] and self.grid[piece.row + row][piece.col + col]:
                    return False
        return True

    def add_piece(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col]:
                    self.grid[piece.row + row][piece.col + col] = piece.color

    def clear_lines(self):
        lines = []
        for row in range(len(self.grid)):
            if all(self.grid[row]):
                lines.append(row)
        for line in lines:
            self.grid.pop(line)
            self.grid.insert(0, [None for _ in range(self.cols)])
        return len(lines)