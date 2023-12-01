import pygame
from board import Board
from utils import assets_library
from decorators.sounds import Sounds
from models.falling_items.points_falling_item import PointsFallingItem
from models.falling_items.damage_falling_item import DamageFallingItem


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board, falling_group):
        super().__init__()
        self.sprites_right = []
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right1']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right2']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right3']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right4']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right5']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right6']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right7']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right8']))
        self.sprites_right.append(pygame.image.load(
            assets_library['sprites']['player']['player_right']['player_right9']))
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left1']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left2']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left3']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left4']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left5']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left6']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left7']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left8']))
        self.sprites_left.append(pygame.image.load(
            assets_library['sprites']['player']['player_left']['player_left9']))
        self.current_sprite = 0
        self.image = pygame.transform.scale(
            self.sprites_right[self.current_sprite], (100, 238))
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
        self.falling_group = falling_group
        self.life = 90
        self.points = 0
        self.level = 1
        self.is_winner = False
        self.leveled_up = False
        self.loser = False


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

    @Sounds(assets_library['sounds']['bonus'], loop=False)
    def points_collision(self, item):
        self.points += item.points
        self.life += item.damage

    @Sounds(assets_library['sounds']['damage'], loop=False)
    def damage_collision(self, item):
        self.points -= item.points
        self.life -= item.damage

    def check_falling_item_collision(self):
        if self.life > 0:
            collisions = pygame.sprite.spritecollide(self, self.falling_group.falling_items, True)
            for item in collisions:
                item.rect.topleft = (-100, -100)
                item.y = 1000
                item.rect.y = 1000
                if isinstance(item, PointsFallingItem):
                    self.points_collision(item)
                if isinstance(item, DamageFallingItem):
                    self.damage_collision(item)
        else:
            self.loser = True
        return self.points, self.loser

    def get_lives(self):
        return self.life

    def get_points(self):
        return self.points

    def get_level(self):
        return self.level

    def get_is_winner(self):
        return self.is_winner

    def check_is_winner(self):
        if self.life > 0 and self.level == 3:
            self.toggle_is_winner()
        return

    def toggle_is_winner(self):
        self.is_winner = not self.is_winner
        return self.is_winner

    def check_for_level_up(self):
        if self.life > 0:
            self.leveled_up = True
            return self.leveled_up
        
    def level_up_player(self):
        self.level += 1
        return self.level
        
    def reset_player_stats(self):
        self.rect.center = (800 - 725, 600 - 200,)
        self.life = 90
        self.points = 0
        self.leveled_up = False
        self.loser = False
        return self.life, self.points, self.leveled_up, self.loser


