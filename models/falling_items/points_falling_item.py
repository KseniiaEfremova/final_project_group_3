from abc import ABC
import datetime
from models.falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, image, speed, damage, points, width, height, x, y, board_instance):
        super().__init__(
            name, image, speed, damage, points, width, height, x, y, board_instance
        )

    def disappear(self, stop_time):
        self.y = 500
        if datetime.datetime.utcnow() > stop_time:
            self.y = 500
            self.rect.y = 500
            self.kill()
            self.spawn()


class TickItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "Tick", image, 5, 0, 1, 50, 50, 0, 0, board_instance
        )


class PythonItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "Python", image, 8, 0, 5, 50, 50, 0, 0, board_instance
        )


class RubberDuckItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "Rubber duck", image, 12, 0, 10, 50, 50, 0, 0, board_instance
        )
