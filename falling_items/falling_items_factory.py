from falling_items.damage_falling_item import *
from falling_items.points_falling_item import *
from board import *
from player import Player
import pygame
from abc import ABC
import datetime
import time
import random


class FallingItemsFactory(ABC, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.timer_seconds = 60
        self.start_time = time.time()
        self.long_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=5)
        self.medium_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=4)
        self.short_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=3)
        self.stop_list = [self.long_stop, self.medium_stop, self.short_stop]

        self.interval = 1000
        self.counter = 0
        self.fall_timer = pygame.USEREVENT + 1

        self.long_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=5)
        self.medium_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=4)
        self.short_stop = datetime.datetime.utcnow() + datetime.timedelta(
            seconds=3)

        self.python_image = pygame.image.load("assets/sprites/python1.png")
        self.tick_image = pygame.image.load("assets/sprites/tick.png")
        self.duck_image = pygame.image.load("assets/sprites/duck5.png")
        self.bug_image = pygame.image.load("assets/sprites/bug1.png")
        self.error_image = pygame.image.load("assets/sprites/error.png")
        self.warning_image = pygame.image.load("assets/sprites/warning.png")
        self.falling_items = pygame.sprite.Group()
        self.game_board = Board('Code Quest', (800, 600), 60)
        self.python = PythonItem(self.python_image, self.game_board)
        self.tick = TickItem(self.tick_image, self.game_board)
        self.duck = RubberDuckItem(self.duck_image, self.game_board)
        self.warning = WarningItem(self.warning_image, self.game_board)
        self.error = ErrorItem(self.error_image, self.game_board)
        self.bug = BugItem(self.bug_image, self.game_board)
        self.item_list = []

    def create_timer(self):
        pygame.time.set_timer(self.fall_timer, self.interval)

    def create_group(self):
        self.item_list = [self.tick, self.duck, self.warning, self.error, self.bug, self.python]
        for item in self.item_list:
            self.falling_items.add(item)

    def set_fall_timer(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == self.fall_timer:
                self.counter += 1
                print(f"Hi from timer: {self.counter}")
                new_sprite = random.choice(self.item_list)
                self.falling_items.add(new_sprite)

                print(f"Falling items added to {self.falling_items}: {new_sprite}")

    def fall_and_respawn(self):
        for sprite in self.falling_items.sprites():
            sprite.draw(self.game_board)
            sprite.fall()
            # if sprite.y >= 500:
            #     sprite.disappear(self.short_stop)
            if self.python.y >= 500:
                self.python.disappear(self.medium_stop)
            if self.tick.y >= 500:
                self.tick.disappear(self.short_stop)
            if self.duck.y >= 500:
                self.duck.disappear(self.long_stop)
            if self.warning.y >= 500:
                self.warning.disappear(self.short_stop)
            if self.error.y >= 500:
                self.error.disappear(self.medium_stop)
            if self.bug.y >= 500:
                self.bug.disappear(self.long_stop)

        if len(self.falling_items) >= 6:
            for item in self.falling_items:
                item.kill()
        if self.python.y >= 500:
            self.python.disappear(self.medium_stop)
        if self.tick.y >= 500:
            self.tick.disappear(self.short_stop)
        if self.duck.y >= 500:
            self.duck.disappear(self.long_stop)
        if self.warning.y >= 500:
            self.warning.disappear(self.short_stop)
        if self.error.y >= 500:
            self.error.disappear(self.medium_stop)
        if self.bug.y >= 500:
            self.bug.disappear(self.long_stop)


