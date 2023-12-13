from falling_items.damage_falling_item import *
from falling_items.points_falling_item import *
from utils import assets_library
from board import *
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

        self.python_image = pygame.image.load(assets_library['sprites']['python']['python1'])
        self.tick_image = pygame.image.load(assets_library['sprites']['tick'])
        self.duck_image = pygame.image.load(assets_library['sprites']['duck']['duck5'])
        self.bug_image = pygame.image.load(assets_library['sprites']['bug']['bug1'])
        self.error_image = pygame.image.load(assets_library['sprites']['error'])
        self.warning_image = pygame.image.load(assets_library['sprites']['warning'])
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
                new_sprite = random.choice(self.item_list)
                self.falling_items.add(new_sprite)

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

    def check_player_collision(self, player):
        collisions = pygame.sprite.spritecollide(player, self.falling_items, False)
        for falling_item in collisions: 
            falling_item.rect.x = -10
            falling_item.rect.y = -10
            falling_item.image = None