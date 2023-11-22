import pygame
import sys
from utils import get_path_from_root

background_image = pygame.image.load("assets/background.jpg")

class Board():
    def __init__(self, name, res, frames):
        self.name = name
        self.res = res
        self.frames = frames
        self.image = pygame.transform.scale(background_image, (self.res))
        self.board = pygame.display.set_mode(self.res)

    def draw_timer(self, timer):
        timer_rect = pygame.Rect(10, 10, 111, 45)
        pygame.draw.rect(self.board, (255, 255, 255), timer_rect)
        pygame.draw.rect(self.board, (0, 0, 0), timer_rect, 2)
        text = font.render("Time: {}".format(timer), True, (0, 0, 0))
        self.board.blit(text, (20, 20))
    
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

    def draw_background(self):
        self.board.blit(self.image, (0, 0))
