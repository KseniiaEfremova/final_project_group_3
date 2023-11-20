from abc import abstractmethod
from abc import ABC
from abstract_falling_item import FallingItem

# class for the items that award player with points


class PointsFallingItem(FallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y):
        super().__init__(
            name, speed, damage, points, width, height, x, y
        )

    def disappear(self):
        return self.y > 600


class TickFallingItem(PointsFallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y):
        super().__init__(
            "tick", 5, 0, 1, 0, 0, 0, 0
        )


class PythonFallingItem(PointsFallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y):
        super().__init__(
            "python", 12, 0, 5, 0, 0, 0, 0
        )


class RubberDuckFallingItem(PointsFallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y):
        super().__init__(
            "rubber duck", 8, 0, 10, 0, 0, 0, 0
        )


ducky = RubberDuckFallingItem()