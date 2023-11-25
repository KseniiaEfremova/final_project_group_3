import pygame
from board import Board


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board):
        super().__init__()
        self.sprites_right = []
        self.sprites_right.append(pygame.image.load("assets/player_idle.png"))
        self.sprites_right.append(pygame.image.load("assets/player1.png"))
        self.sprites_right.append(pygame.image.load("assets/player2.png"))
        self.sprites_right.append(pygame.image.load("assets/player3.png"))
        self.sprites_right.append(pygame.image.load("assets/player4.png"))
        self.sprites_right.append(pygame.image.load("assets/player5.png"))
        self.sprites_right.append(pygame.image.load("assets/player6.png"))
        self.sprites_right.append(pygame.image.load("assets/player7.png"))
        self.sprites_right.append(pygame.image.load("assets/player8.png"))
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load("assets/player_idle_left.png"))
        self.sprites_left.append(pygame.image.load("assets/player9.png"))
        self.sprites_left.append(pygame.image.load("assets/player10.png"))
        self.sprites_left.append(pygame.image.load("assets/player11.png"))
        self.sprites_left.append(pygame.image.load("assets/player12.png"))
        self.sprites_left.append(pygame.image.load("assets/player13.png"))
        self.sprites_left.append(pygame.image.load("assets/player14.png"))
        self.sprites_left.append(pygame.image.load("assets/player15.png"))
        self.sprites_left.append(pygame.image.load("assets/player16.png"))
        self.current_sprite = 0
        self.image = pygame.transform.scale(
            self.sprites_right[self.current_sprite], (100, 238))
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
        self.life = 90
        self.points = 0
        self.level = 1

    def draw_player(self):
        self.board_instance.board.blit(self.image, (self.rect.x,
                                                    self.rect.y - 10))

    def constrain_move_within_board(self, dx, dy):
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > self.board_instance.res[0]:
            dx = self.board_instance.res[0] - self.rect.right
        return dx, dy

    def animate(self, direction):
        self.current_sprite += 1
        if self.current_sprite >= 8:
            self.current_sprite = 0
        if direction == 'right':
            self.image = self.sprites_right[self.current_sprite]
            self.image = pygame.transform.scale(self.sprites_right[self.current_sprite],
                                            (100, 238))
        else:
            self.image = self.sprites_left[self.current_sprite]
            self.image = pygame.transform.scale(self.sprites_left[self.current_sprite],
                                            (100, 238))


    def move(self):
        # variable to reset for delta x and delta y
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
            self.animate('left')
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10
            self.animate('right')
        dx, dy = self.constrain_move_within_board(dx, dy)    

        self.rect.x += dx
        self.rect.y += dy
        