from game.core.config import *
import pygame
from game.pygame.events import *


class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.font_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.grid_color = (50, 50, 50)
        self.current_piece  = Piece.new_pieces()

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.font_color)
        self.screen.blit(text_surface, (x, y))
    
    def draw_grid(self, grid):
        for row in range(grid_rows):
            for col in range(grid_cols):
                if grid[row][col]:
                    pygame.draw.rect(self.screen, grid[row][col], 
                                     (game_zone_x + col * block_size, 
                                      game_zone_y + row * block_size, 
                                      block_size, block_size))
        for row in range(grid_rows + 1):
            pygame.draw.line(self.screen, self.grid_color, 
                             (game_zone_x, game_zone_y + row * block_size), 
                             (game_zone_x + grid_cols * block_size, 
                              game_zone_y + row * block_size))
        for col in range(grid_cols + 1):
            pygame.draw.line(self.screen, self.grid_color, 
                             (game_zone_x + col * block_size, game_zone_y), 
                             (game_zone_x + col * block_size, 
                              game_zone_y + grid_rows * block_size))
            
    def draw_pieces(self, screen):
        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        pygame.draw.rect(screen, self.current_piece.color, 
                                        ((self.current_piece.x + j) * GRID_SIZE,
                                        (self.current_piece.y + i) * GRID_SIZE,
                                        GRID_SIZE - 1, GRID_SIZE - 1))

    def draw(self, grid, score):
        self.screen.fill(self.background_color)
        self.draw_grid(grid)
        self.draw_text(f"Score: {score}", 20, 20)
        pygame.display.flip()    
    
    

    def draw_game_over(screen, x, y):
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (x, y))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    display = Display(screen)
    test_grid = [[None for _ in range(grid_cols)] for _ in range(grid_rows)]  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.draw(test_grid, 0)
        pygame.time.delay(100)
        Events(display).run(display)
    pygame.quit()
