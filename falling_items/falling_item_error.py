from abstract_falling_item import FallingItem
import random

class ErrorItem(FallingItem):
    def __init__(self, board_width):
        super().__init__('Error', 8, 10, -5, 30, 30, 0, 0)
        self.board_width = board_width
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, self.board_width - self.width)
        self.y = 0

    def fall(self):
        self.y += self.speed

    def disappear(self):
        return self.y > 600
    