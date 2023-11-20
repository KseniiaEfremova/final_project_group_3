from abstract_falling_item import FallingItem
import random

class DamageFallingItem(FallingItem):
    def __init__(self, name, speed, points, width, height, x, y, board_width):
        super().__init__(name, speed, 0, points, width, height, x, y, board_width)
    
class ErrorItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Error', 8, 10, -5, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (255, 0, 255), (self.x, self.y, self.width, self.height))
    
class BugItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Bug', 3, 30, -10, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (245, 245, 245), (self.x, self.y, self.width, self.height))
    
class WarningItem(DamageFallingItem):
    def __init__(self, board_width):
        super().__init__('Warning', 5, 1, -1, 30, 30, 0, 0, board_width)

    def disappear(self):
        return self.y > 600
    
    def draw(self, board_instance):
        pygame.draw.rect(board_instance.board, (235,20, 50), (self.x, self.y, self.width, self.height))


    
