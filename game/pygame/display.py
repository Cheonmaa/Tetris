import pygame
from game.core.config import *
from game.core.grid import Grid
from game.core.pieces import Piece

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.font_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.grid_color = (50, 50, 50)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.font_color)
        self.screen.blit(text_surface, (x, y))
    
    def draw_grid(self, grid):
        for row in range(grid.rows):
            for col in range(grid.cols):
                if grid.grid[row, col]:
                    pygame.draw.rect(self.screen, COLORS[grid.grid[row, col] - 1],
                                     (game_zone_x + col * block_size, 
                                      game_zone_y + row * block_size, 
                                      block_size, block_size))
        for row in range(grid.rows + 1):
            pygame.draw.line(self.screen, self.grid_color, 
                             (game_zone_x, game_zone_y + row * block_size), 
                             (game_zone_x + grid.cols * block_size, 
                              game_zone_y + row * block_size))
        for col in range(grid.cols + 1):
            pygame.draw.line(self.screen, self.grid_color, 
                             (game_zone_x + col * block_size, game_zone_y), 
                             (game_zone_x + col * block_size, 
                              game_zone_y + grid.rows * block_size))
            
    def draw_piece(self, piece):
        for i, row in enumerate(piece.get_rotated_shape()):
            for j, cell in enumerate(row):
                if cell == 'O':
                    pygame.draw.rect(self.screen, piece.color, 
                                     ((game_zone_x + (piece.col + j) * block_size),
                                      (game_zone_y + (piece.row + i) * block_size),
                                      block_size - 1, block_size - 1))
    
    def draw(self, grid, piece, score):
        self.screen.fill(self.background_color)
        self.draw_grid(grid)
        self.draw_piece(piece)
        self.draw_text(f"Score: {score}", 20, 20)
        pygame.display.flip()
    
    def draw_game_over(self):
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, RED)
        self.screen.blit(text, (window_width // 2 - 60, window_height // 2 - 20))
        pygame.display.flip()
