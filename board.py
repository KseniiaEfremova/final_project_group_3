import pygame
import sys

class Board():
    def __init__(self, name, res, frames):
        self.name = name
        self.res = res
        self.frames = frames
        self.board = pygame.display.set_mode(self.res)

    def display_board(self):
        pygame.display.set_caption(self.name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_display(self):
        fps = pygame.time.Clock()
        pygame.display.update()
        fps.tick(self.frames)
