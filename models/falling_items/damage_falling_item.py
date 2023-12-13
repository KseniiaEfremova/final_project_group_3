from abc import ABC
import pygame
import datetime
from models.falling_items.abstract_falling_item import FallingItem


class DamageFallingItem(FallingItem, ABC):
    """
    A falling item that causes damage when colliding with the player in Code Quest.

    Attributes:
        name (str): The name of the damage falling item.
        image (pygame.Surface): The image representing the damage falling item.
        speed (int): The speed at which the damage falling item descends.
        damage (int): The amount of damage inflicted by the falling item.
        points (int): The points awarded for catching the falling item.
        width (int): The width of the falling item.
        height (int): The height of the falling item.
        x (int): The x-coordinate of the falling item's current position.
        y (int): The y-coordinate of the falling item's current position.
        board_instance (Board): An instance of the game board.
        disappear_start_time (datetime.datetime): The time at which the falling item starts disappearing.
    """
    
    def __init__(self, name, image,  speed, damage, points, width, height, x, y,
                 board_instance):
        """
        Initialises a DamageFallingItem object.

        Parameters:
            name (str): The name of the damage falling item.
            image (pygame.Surface): The image representing the damage falling item.
            speed (int): The speed at which the damage falling item descends.
            damage (int): The amount of damage inflicted by the falling item.
            points (int): The points awarded for catching the falling item.
            width (int): The width of the falling item.
            height (int): The height of the falling item.
            x (int): The x-coordinate of the falling item's initial position.
            y (int): The y-coordinate of the falling item's initial position.
            board_instance (Board): An instance of the game board.
        """
        super().__init__(name, image, speed, damage, points, width, height, x,
                         y, board_instance)
        self.image = pygame.transform.scale(image, (50, 50))
        self.disappear_start_time = None
    
    def disappear(self):
        """
        Make the falling item blow up to a larger scale and disappear at the stop_time.
        then handle its respawn.
        """
        self.y = 500
        current_time = datetime.datetime.utcnow()
        elapsed_time = current_time - self.stop_time

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
        if datetime.datetime.utcnow() > self.stop_time:
            self.kill()
            self.spawn()
            self.stop_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)


class ErrorItem(DamageFallingItem):
    """
    A falling item representing an error in Code Quest.

    Attributes:
        image (pygame.Surface): The image representing the error falling item.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):
        """
        Initialises an ErrorItem object.

        Parameters:
            image (pygame.Surface): The image representing the error falling item.
            board_instance (Board): An instance of the game board.
        """
        super().__init__('Error', image,  5, 10, 5,
                         50, 50, 0, 0, board_instance)


class BugItem(DamageFallingItem):
    """
    A falling item representing a bug in Code Quest.

    Attributes:
        image (pygame.Surface): The image representing the bug falling item.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):
        """
        Initialises a BugItem object.

        Parameters:
            image (pygame.Surface): The image representing the bug falling item.
            board_instance (Board): An instance of the game board.
        """
        super().__init__('Bug', image,  8, 30, 10,
                         50, 50, 0, 0, board_instance)


class WarningItem(DamageFallingItem):
    """
    A falling item representing a warning in Code Quest.

    Attributes:
        image (pygame.Surface): The image representing the warning falling item.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):
        """
        Initialises a WarningItem object.

        Parameters:
            image (pygame.Surface): The image representing the warning falling item.
            board_instance (Board): An instance of the game board.
        """
        super().__init__('Warning', image, 12, 1, 1,
                         50, 50, 0, 0, board_instance)
