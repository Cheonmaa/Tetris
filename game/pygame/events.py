from game.core.pieces import *
import pygame
import os

#Disable os sound -> Problem with WSL
os.environ["SDL_AUDIODRIVER"] = "dummy"

class Events:
    def __init__(self, display):
        self.run(display)

    def rotate_key(self, display):
        color = (255,12,15)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                display.fill(color)
                pygame.display.flip()
                print("Touche R pressée !")

    def run(self, display):
        running = True
        while running:
            self.rotate_key(display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()

if __name__ == "__main__":
    Events()
