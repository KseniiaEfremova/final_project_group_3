from abstract_falling_item import FallingItem

# class for the items that award player with points
# inheriting from abstract class FallingItem


class PointsFallingItem(FallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y, board_width):
        super().__init__(
            name, speed, damage, points, width, height, x, y, board_width
        )

    def disappear(self):
        return self.y > 600


# subclasses that will make up three different items awarding player with points
class TickFallingItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "tick", 5, 0, 1, 0, 0, 0, 0, board_width
        )


class PythonFallingItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "python", 12, 0, 5, 0, 0, 0, 0, board_width
        )


class RubberDuckFallingItem(PointsFallingItem):
    def __init__(self, board_width):
        super().__init__(
            "rubber duck", 8, 0, 10, 0, 0, 0, 0, board_width
        )
