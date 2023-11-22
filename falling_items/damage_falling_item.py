from abc import ABC
import pygame
import datetime
from falling_items.abstract_falling_item import FallingItem


class DamageFallingItem(FallingItem, ABC):
    def __init__(self, name, speed, points, damage, width, height, x, y, board_width):
        super().__init__(name, speed, points, damage, width, height, x, y, board_width)
    
    def disappear(self, stop_time):
        self.y = 500
        if datetime.datetime.utcnow() > stop_time:
            self.y = 700
            self.kill()


class ErrorItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Error', 8, 0,30, 30, 30, 0, 0,  board_width)

    def disappear(self, stop_time):
        pass
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (255, 0, 255), (self.x, self.y, self.width, self.height))


class BugItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Bug', 3, 0, 10, 30, 30, 0, 0, board_width)

    def disappear(self, stop_time):
        pass
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (245, 245, 245), (self.x, self.y, self.width, self.height))

class WarningItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Warning', 5, 0,5,  30, 30, 0, 0,  board_width)

    def disappear(self, stop_time):
        pass
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (235,20, 50), (self.x, self.y, self.width, self.height))

    
