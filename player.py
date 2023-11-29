import pygame
from board import Board
from utils import assets_library
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, board_instance: Board, python_instance: PythonItem, tick_instance: TickItem, duck_instance: RubberDuckItem, warning_instance: WarningItem, error_instance: ErrorItem, bug_instance: BugItem):        
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
        self.leveled_up = False
        
        
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
        if self.life - self.damage > 0:
            if self.rect.colliderect(self.python_instance.rect):
                print("You have hit the Python")
                self.points += self.python_instance.points
                self.damage += self.python_instance.damage
                self.python_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")

            elif self.rect.colliderect(self.tick_instance.rect):
                print("You have hit the tick")
                self.points += self.tick_instance.points
                self.damage += self.tick_instance.damage
                self.tick_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
            
            elif self.rect.colliderect(self.duck_instance.rect):
                print("You have hit the Duck")
                self.points += self.duck_instance.points
                self.damage += self.duck_instance.damage
                self.duck_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
                
            elif self.rect.colliderect(self.warning_instance.rect):
                print("You have hit the Warning")
                self.points += self.warning_instance.points
                self.damage += self.warning_instance.damage
                self.warning_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
                
            elif self.rect.colliderect(self.error_instance.rect):
                print("You have hit the Error")
                self.points += self.error_instance.points
                self.damage += self.error_instance.damage
                self.error_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
                
            elif self.rect.colliderect(self.bug_instance.rect):
                print("You have hit the Bug")
                self.points += self.bug_instance.points
                self.damage += self.bug_instance.damage
                self.bug_instance.rect.topleft = (-100, -100)
                print(f"The Player now has: {self.points} points, and {self.damage} damage")
        else:
            self.kill()
            print(f"Game Over! You now have {self.life - self.damage} life points left")
            # We can add additional game over logic here, like displaying a game over screen
            pygame.quit()
            sys.exit()
        return self.points, self.damage
        

    def check_for_level_up(self):
        if self.life > 0:
            self.level += 1
            self.life = 90
            self.leveled_up = True
            print(f"Level Up! You are now at Level {self.level}")
            return self.level, self.life
            # pygame.quit()
            # sys.exit()
            
