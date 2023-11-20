from abstract_falling_item import FallingItem
import random

class DamageFallingItem(FallingItem):
    pass

class ErrorItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Error', 8, 10, -5, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600
    
class BugItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Bug', 3, 30, -10, 30, 30, 0, 0, board_width)
    def disappear(self):
        return self.y > 600
    
class WarningItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Warning', 5, 1, -1, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600


    
