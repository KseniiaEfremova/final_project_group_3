from abc import ABC
import pygame
import datetime
from falling_items.abstract_falling_item import FallingItem


class DamageFallingItem(FallingItem, ABC):
    def __init__(self, name, image,  speed, points, damage, width, height, x, y, board_width, board_instance):
        super().__init__(name, image, speed, points, damage, width, height, x, y, board_width, board_instance)
        self.image = pygame.transform.scale(image, (30, 30))
    
    def disappear(self, stop_time):
        self.y = 500
        transparent = (0, 0, 0, 0)
        blow = pygame.transform.scale(self.image, (90, 90))
        self.board_instance.board.blit(blow,
                                       (self.x, self.y))
        if datetime.datetime.utcnow() > stop_time:
            self.y = 700
            self.image.fill(transparent)
            self.kill()


class ErrorItem(DamageFallingItem):
    def __init__(self, image, board_width, board_instance):
        super().__init__('Error', image,  8, 0,30, 30, 30, 0, 0,  board_width, board_instance)

    # def disappear(self, stop_time):
    #     pass
    
    def draw(self, board_instance):
        board_instance.board.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(board_instance.board, (255, 0, 255), (self.x, self.y, self.width, self.height))


class BugItem(DamageFallingItem):
    def __init__(self, image, board_width, board_instance):
        super().__init__('Bug', image,  3, 0, 10, 30, 30, 0, 0, board_width, board_instance)

    # def disappear(self, stop_time):
    #     pass
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (245, 245, 245), (self.x, self.y, self.width, self.height))


class WarningItem(DamageFallingItem):
    def __init__(self, image, board_width, board_instance):
        super().__init__('Warning', image, 5, 0,5,  30, 30, 0, 0,  board_width, board_instance)

    # def disappear(self, stop_time):
    #     pass
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (235, 20, 50), (self.x, self.y, self.width, self.height))

    
