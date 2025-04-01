import pygame
import time
import os
from game.core.config import *
from game.core.grid import Grid
from game.core.pieces import Piece
from game.pygame.display import Display
from game.pygame.events import Events
from game.core.score import Score

# Disable OS sound -> Problem with WSL
os.environ["SDL_AUDIODRIVER"] = "dummy"


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(game_title)
        
        self.grid = Grid()
        self.display = Display(self.screen)
        self.events = Events()
        self.piece = Piece()
        self.score = Score()
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        fall_time = 0
        
        while self.running:
            self.events.handle_events(self.piece, self.grid)
            fall_time += clock.get_rawtime()
            clock.tick(game_fps)
            
            if fall_time / 1000 >= fall_speed:
                if not self.piece.move_down(self.grid):
                    self.grid.add_piece(self.piece)
                    self.score.add(self.grid.clear_lines() * 10)
                    self.piece = Piece()
                    if not self.grid.is_valid_position(self.piece):
                        self.running = False
                fall_time = 0
            
            self.display.draw(self.grid, self.piece, self.score.get())
            
        self.display.draw_game_over()
        time.sleep(2)
        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()