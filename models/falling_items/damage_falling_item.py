from abc import ABC
import pygame
import datetime
from models.falling_items.abstract_falling_item import FallingItem


class DamageFallingItem(FallingItem, ABC):
    def __init__(self, name, image,  speed, damage, points, width, height, x, y,
                 board_instance):
        super().__init__(name, image, speed, damage, points, width, height, x,
                         y, board_instance)
        self.image = pygame.transform.scale(image, (50, 50))
        self.disappear_start_time = None

    def draw(self, board_instance):
        board_instance.board.blit(self.image, (self.x, self.y))
    
    def disappear(self, stop_time):
        self.y = 500
        current_time = datetime.datetime.utcnow()
        elapsed_time = current_time - stop_time

        if elapsed_time <= datetime.timedelta(seconds=3):
            disappearance_progress = -(elapsed_time.total_seconds() / 3)

            initial_width = self.width
            initial_height = self.height
            scaled_width = int(initial_width + 90 * (1 - disappearance_progress))
            scaled_height = int(initial_height + 90 * (1 - disappearance_progress))

            final_width = max(scaled_width, initial_width)
            final_height = max(scaled_height, initial_height)

            blow = pygame.transform.scale(self.image,
                                          (final_width, final_height))

            offset_x = self.x - (final_width - initial_width) // 2
            offset_y = self.y - (final_height - initial_height) // 2

            self.board_instance.board.blit(blow, (offset_x, offset_y))
        if datetime.datetime.utcnow() > stop_time:
            # self.y = 500
            self.kill()
            self.spawn()


class ErrorItem(DamageFallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Error', image,  5, 10, 5,
                         50, 50, 0, 0, board_instance)


class BugItem(DamageFallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Bug', image,  8, 30, 10,
                         50, 50, 0, 0, board_instance)


class WarningItem(DamageFallingItem):
    def __init__(self, image, board_instance):
        super().__init__('Warning', image, 12, 1, 1,
                         50, 50, 0, 0, board_instance)

    



    
