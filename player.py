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
        
        
    def constrain_move_within_board(self, dx, dy):
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > self.board_instance.res[0]:
            dx = self.board_instance.res[0] - self.rect.right
        return dx, dy
    

    def move(self):
        # variable to reset for delta x and delta y
        dx = 0
        dy = 0     
        # look for key presses and update dx
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10
        # constrain move to stop player going off edge of board
        dx, dy = self.constrain_move_within_board(dx, dy)    
        # move rectangle
        self.rect.x += dx
        self.rect.y += dy
        