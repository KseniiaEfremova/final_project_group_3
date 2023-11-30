from abc import ABC
import datetime
from models.falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, image, speed, damage, points, width, height, x, y, board_instance):
        super().__init__(
            name, image, speed, damage, points, width, height, x, y, board_instance
        )

    def disappear(self):
        self.y = 500
        if datetime.datetime.utcnow() > self.stop_time:
            self.y = 500
            self.rect.y = 500
            self.kill()
            self.spawn()
            self.stop_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)


class TickItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "tick", image, 5, 0, 1, 30, 30, 0, 0, board_instance
        )


class PythonItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "python", image, 8, 0, 5, 30, 30, 0, 0, board_instance
        )


class RubberDuckItem(PointsFallingItem, ABC):
    def __init__(self, image, board_instance):
        super().__init__(
            "rubber duck", image, 12, 0, 10, 30, 30, 0, 0, board_instance
        )
