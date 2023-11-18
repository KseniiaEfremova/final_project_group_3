import pygame
from board import Board


# load player image
player_image = pygame.image.load("assets/player.png")

# Player class
class Player(): 
    def __init__(self, x, y, board_instance: Board):
        self.image = pygame.transform.scale(player_image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.board_instance = board_instance

    def draw_player(self):
        self.board_instance.board.blit(self.image, self.rect)
        