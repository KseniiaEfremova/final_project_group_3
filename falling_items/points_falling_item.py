from abc import ABC
from abc import abstractmethod
import pygame.draw
from falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, speed, damage, points, width, height, x, y, board_width):
        super().__init__(
            name, speed, damage, points, width, height, x, y, board_width
        )

    @abstractmethod
    def disappear(self):
        pass


class TickItem(PointsFallingItem, ABC):
    def __init__(self, board_width):
        super().__init__(
            "tick", 5, 0, 1, 30, 30, 0, 0, board_width
        )

    # def disappear(self):
    #     return self.y > 600

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (166, 204, 112),
                         (self.x, self.y, self.width, self.height))


class PythonItem(PointsFallingItem, ABC):
    def __init__(self, board_width):
        super().__init__(
            "python", 12, 0, 5, 30, 30, 0, 0, board_width
        )

    def disappear(self):
        self.y = 500

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (47, 111, 55),
                         (self.x, self.y, self.width, self.height))


class RubberDuckItem(PointsFallingItem, ABC):
    def __init__(self, board_width):
        super().__init__(
            "rubber duck", 8, 0, 10, 30, 30, 0, 0, board_width
        )

    # def disappear(self):
    #     return self.y > 600

    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (244, 230, 87),
                         (self.x, self.y, self.width, self.height))
