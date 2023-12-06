import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font(None, 24)


class PopupWindow:
    def __init__(self, width, height, text, x=0, y=0, opened=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.opened = opened

    def draw_window(self, board):
        color = pygame.Color('brown2')
        pygame.draw.rect(board, color, self.rect)
        text_surface = font.render(self.text, True, (255, 255, 255))

        location = text_surface.get_rect()
        start_text = int(self.rect.width / 2 - location.center[0])

        board.blit(text_surface, (self.rect.x + start_text, self.rect.y + 12))
        self.opened = True
