import pygame
from board import Board

# load player image
player_image = pygame.image.load("assets/player.png")

# Player class
class Player(): 
    def __init__(self, x, y, board_instance: Board):
        self.image = pygame.transform.scale(player_image, (100, 100))
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
        

    def draw_player(self):
        self.board_instance.board.blit(self.image, (self.rect.x, self.rect.y - 10))
        #pygame.draw.rect(self.board_instance.board, (255, 255, 255), self.rect, 2)
        
    def move(self):
        # look for key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.rect.x += 10
            
            