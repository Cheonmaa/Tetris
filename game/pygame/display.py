from game.core.config import *
import pygame


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

    def draw(self, grid, score):
        self.screen.fill(self.background_color)
        self.draw_grid(grid)
        self.draw_text(f"Score: {score}", 20, 20)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    display = Display(screen)
    test_grid = [[None for _ in range(grid_cols)] for _ in range(grid_rows)]
    test_grid[5][3] = COLORS['T']    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.draw(test_grid, 100)
        pygame.time.delay(100)
    pygame.quit()
