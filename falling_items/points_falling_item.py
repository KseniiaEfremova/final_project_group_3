from abc import ABC
import datetime
from falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, image, speed, damage, points, width, height, x, y, board_instance):
        super().__init__(
            name, image, speed, damage, points, width, height, x, y, board_instance
        )

    def draw(self, board_instance):
            board_instance.board.blit(self.image, (self.x, self.y))

    def disappear(self, stop_time):
        self.y = 500
        if datetime.datetime.utcnow() > stop_time:
            self.y = 700
            self.kill()


class TickItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "tick", image, 5, 1, 0, 30, 30, 0, 0, board_instance
        )


class PythonItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "python", image, 12, 5, 0, 30, 30, 0, 0, board_instance
        )


class RubberDuckItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "rubber duck", image, 8, 10, 0, 30, 30, 0, 0, board_instance
        )
