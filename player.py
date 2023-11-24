import pygame
from board import Board

player_image = pygame.image.load("assets/player_idle.png")


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("assets/player_idle.png"))
        self.sprites.append(pygame.image.load("assets/player1.png"))
        self.sprites.append(pygame.image.load("assets/player2.png"))
        self.sprites.append(pygame.image.load("assets/player3.png"))
        self.sprites.append(pygame.image.load("assets/player4.png"))
        self.sprites.append(pygame.image.load("assets/player5.png"))
        self.sprites.append(pygame.image.load("assets/player6.png"))
        self.sprites.append(pygame.image.load("assets/player7.png"))
        self.sprites.append(pygame.image.load("assets/player8.png"))
        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 238))
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance

    def draw_player(self):
        self.board_instance.board.blit(self.image, (self.rect.x,
                                                    self.rect.y - 10))

    def constrain_move_within_board(self, dx, dy):
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > self.board_instance.res[0]:
            dx = self.board_instance.res[0] - self.rect.right
        return dx, dy

    def animate(self):
        self.current_sprite += 1
        if self.current_sprite >= 8:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.sprites[self.current_sprite],
                                            (100, 238))

    def move(self):
        # variable to reset for delta x and delta y
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
            self.animate()
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10
            self.animate()
        dx, dy = self.constrain_move_within_board(dx, dy)    

        self.rect.x += dx
        self.rect.y += dy
        