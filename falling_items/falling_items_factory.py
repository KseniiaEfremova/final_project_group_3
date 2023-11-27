from points_falling_item import TickItem, PythonItem, RubberDuckItem
from damage_falling_item import ErrorItem, BugItem, WarningItem
import pygame
from abc import ABC
import datetime
import time
import random

class FallingItemsFactory(ABC):
    def __init__(self):
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

        self.python_image = None
        self.tick_image = None
        self.duck_image = None
        self.bug_image = None
        self.error_image = None
        self.warning_image = None

        self.load_assets()

    def load_assets(self):
        self.python_image = pygame.image.load("assets/sprites/python1.png")
        self.tick_image = pygame.image.load("assets/sprites/tick.png")
        self.duck_image = pygame.image.load("assets/sprites/duck5.png")
        self.bug_image = pygame.image.load("assets/sprites/bug1.png")
        self.error_image = pygame.image.load("assets/sprites/error.png")
        self.warning_image = pygame.image.load("assets/sprites/warning.png")

    def create_timer(self):
        pygame.time.set_timer(self.fall_timer, self.interval)


    def create_group(self):
        self.falling_items = pygame.sprite.Group()
        self.item_list = [self.tick, self., self.warning, self.error, self.bug, self.python]
        for item in self.item_list:
            self.falling_items.add(item)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == self.fall_timer:
                self.counter += 1
                print(f"Hi from timer: {self.counter}")
                new_sprite = random.choice(item_list)
                falling_items.add(new_sprite)

                print(f"Falling items added to {falling_items}: {new_sprite}")

