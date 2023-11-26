from abc import ABC
import datetime
import pygame
from falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):
    def __init__(self, name, image, speed, damage, points, width, height, x, y, board_instance):
        super().__init__(
            name, image, speed, damage, points, width, height, x, y, board_instance
        )

    def disappear(self, stop_time):
        self.y = 500
        transparent = (0, 0, 0, 0)
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
            self.y = 700
            self.kill()
            self.spawn()


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
