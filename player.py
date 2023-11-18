import pygame
from board import Board


# load player image
player_image = pygame.image.load("assets/player.png")

# Player class
class Player(): 
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player_image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        