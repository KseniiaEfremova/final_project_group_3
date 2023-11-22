from abc import ABC

import pygame.draw
from abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, speed, damage, points, width, height, x, y, board_width):
        super().__init__(
            name, speed, damage, points, width, height, x, y, board_width
        )

    def disappear(self):
        return self.y > 600


# subclasses that will make up three different items awarding player with points
class TickItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "tick", 5, 0, 1, 30, 30, 0, 0, board_width
        )

    def disappear(self):  # adding this method to every subclass, so it can be overwritten in the future
        return self.y > 600

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (166, 204, 112),
                         (self.x, self.y, self.width, self.height))


class PythonItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "python", 12, 0, 5, 30, 30, 0, 0, board_width
        )

    def disappear(self):
        return self.y > 600

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (47, 111, 55),
                         (self.x, self.y, self.width, self.height))


class RubberDuckItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "rubber duck", 8, 0, 10, 30, 30, 0, 0, board_width
        )

    def disappear(self):
        return self.y > 600

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (244, 230, 87),
                         (self.x, self.y, self.width, self.height))
