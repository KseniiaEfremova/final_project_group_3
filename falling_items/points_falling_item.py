from abstract_falling_item import FallingItem

# class for the items that award player with points


class PointsFallingItem(FallingItem):
    def __init__(self, name, speed, damage, points, width, height, x, y):
        super().__init__(
            name, speed, damage, points, width, height, x, y
        )

    def spawn(self):
        pass

    def fall(self):
        pass

    def disappear(self):
        pass


# creating three instances of the PointsFallingItem class
PointsFallingItem1 = PointsFallingItem("tick", 5, 0, 1, 0, 0, 0, 0)

PointsFallingItem2 = PointsFallingItem("python", 12, 0, 5, 0, 0, 0, 0)

PointsFallingItem3 = PointsFallingItem("rubber duck", 8, 0, 10, 0, 0, 0, 0)

