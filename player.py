import pygame
from board import Board
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
from typing import List
from falling_items.abstract_falling_item import FallingItem
import datetime

player_image = pygame.image.load("assets/player.png")


class Player:
    def __init__(self, x, y, lives, damage, points, board_instance: Board, python_instance: PythonItem, tick_instance: TickItem, duck_instance: RubberDuckItem, warning_instance: WarningItem, error_instance: ErrorItem, bug_instance: BugItem):
        self.image = pygame.transform.scale(player_image, (100, 100))
        self.lives = lives
        self.damage = damage
        self.points = points
        self.width = 100
        self.height = 90
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
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

    def move(self):
        # variable to reset for delta x and delta y
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -10
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = 10

        dx, dy = self.constrain_move_within_board(dx, dy)    

        self.rect.x += dx
        self.rect.y += dy
        
    
    def check_falling_item_collision(self):
        print(self.python_instance.rect)
        if self.rect.colliderect(self.python_instance.rect):
            self.height = 300
            print("You have hit the Python")
            self.points += self.python_instance.points
            self.damage += self.python_instance.damage
            self.python_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")

        elif self.rect.colliderect(self.tick_instance.rect):
            self.height = 300
            print("You have hit the tick")
            self.points += self.tick_instance.points
            self.damage += self.tick_instance.damage
            self.tick_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.duck_instance.rect):
            self.height = 300
            print("You have hit the Duck")
            self.points += self.duck_instance.points
            self.damage += self.duck_instance.damage
            self.duck_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.warning_instance.rect):
            self.height = 300
            print("You have hit the Warning")
            self.points += self.warning_instance.points
            self.damage += self.warning_instance.damage
            self.warning_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.error_instance.rect):
            self.height = 300
            print("You have hit the Error")
            self.points += self.error_instance.points
            self.damage += self.error_instance.damage
            self.error_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
            
        elif self.rect.colliderect(self.bug_instance.rect):
            self.height = 300
            print("You have hit the Bug")
            self.points += self.bug_instance.points
            self.damage += self.bug_instance.damage
            self.bug_instance.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))
            print(f"Player Points: {self.points}, Player Damage: {self.damage}")
    
    # If I get the above working I will try to put it in a list to simplify
    # def check_falling_item_collision(self):
    #     for falling_item in self.falling_items:
    #         if self.rect.colliderect(falling_item.rect):
    #             self.height = 300
    #             print(f"You have hit the {falling_item.name}")

    #             # Update player's points and damage 
    #             self.points += falling_item.points
    #             self.damage += falling_item.damage

    #             falling_item.disappear(datetime.datetime.utcnow() + datetime.timedelta(seconds=3))

    #             print(f"Player Points: {self.points}, Player Damage: {self.damage}")
