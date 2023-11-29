import pygame
from board import Board
from utils import assets_library
from models.falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem, PointsFallingItem
from models.falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem, DamageFallingItem


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board, falling_group, python_instance: PythonItem, tick_instance: TickItem, duck_instance: RubberDuckItem, warning_instance: WarningItem, error_instance: ErrorItem, bug_instance: BugItem):
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
        self.damage = 0
        self.level = 1
        self.python_instance = python_instance
        self.tick_instance = tick_instance
        self.duck_instance = duck_instance
        self.warning_instance = warning_instance
        self.error_instance = error_instance
        self.bug_instance = bug_instance

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

    def check_falling_item_collision(self):
        collisions = pygame.sprite.spritecollide(self, self.falling_group.falling_items, True)
        for item in collisions:
            if isinstance(item, PointsFallingItem):
                item.rect.topleft = (-100, -100)
                self.points += item.points
                self.damage += item.damage
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
            if isinstance(item, DamageFallingItem):
                item.rect.topleft = (-100, -100)
                self.points -= item.points
                self.damage += item.damage
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
        return self.points, self.damage
