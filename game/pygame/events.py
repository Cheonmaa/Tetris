import pygame
import os
from game.core.pieces import *

class Events:
    def __init__(self):
        self.running = True

    def handle_events(self, piece, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    piece.rotate()
                    if not grid.is_valid_position(piece):
                        piece.rotate()  # Annuler si non valide
                elif event.key == pygame.K_LEFT:
                    piece.move_left(grid)
                elif event.key == pygame.K_RIGHT:
                    piece.move_right(grid)
                elif event.key == pygame.K_DOWN:
                    piece.move_down(grid)
    
    def is_running(self):
        return self.running