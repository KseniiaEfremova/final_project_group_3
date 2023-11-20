from abstract_falling_item import FallingItem
import random

class ErrorItem(FallingItem):
    def __init__(self, board_width):
        super().__init__('Error', 8, 10, -5, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600
    
