from abc import ABC
import pygame
import datetime
import random
from falling_items.abstract_falling_item import FallingItem


class FallingItem(FallingItem, ABC):
    def __init__(self, name, image, speed, damage, points, width, height, x, y,
                 board_instance):
        super().__init__(name, image, speed, damage, points, width, height, x,
                         y, board_instance)

    def update(self):
        # Update the position of the falling item based on its falling speed
        self.y += self.speed
        if self.y > 500:
            # Reset the position if the falling item goes off the screen
            self.y = 0
            self.x = random.randint(0, 750)

    def draw(self, board_instance):
        board_instance.board.blit(self.image, (self.x, self.y))


class ErrorItem(FallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Error', image, 5, 1, 0, 50, 50, 0, 0, board_instance)


class BugItem(FallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Bug', image, 8, 5, 0, 50, 50, 0, 0, board_instance)


class WarningItem(FallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Warning', image, 12, 10, 0, 50, 50, 0, 0, board_instance)