from abc import ABC
import datetime
from models.falling_items.abstract_falling_item import FallingItem


class PointsFallingItem(FallingItem, ABC):

    """
    Abstract base class for points-awarding falling items in Code Quest.

    Attributes:
        name (str): The name of the falling item.
        image (pygame.Surface): The image representing the falling item.
        speed (int): The falling speed of the item.
        damage (int): The damage the item can inflict (unused for points items).
        points (int): The points awarded when the item is collected.
        width (int): The width of the falling item's rect.
        height (int): The height of the falling item's rect.
        x (int): The initial x-coordinate of the falling item.
        y (int): The initial y-coordinate of the falling item.
        board_instance (Board): An instance of the game board.
        stop_time (datetime.datetime): The time when the item should disappear.
    """
    
    def __init__(self, name, image, speed, damage, points, width, height, x, y, board_instance):

        """
        Initialise a PointsFallingItem object.

        Parameters:
            name (str): The name of the falling item.
            image (pygame.Surface): The image representing the falling item.
            speed (int): The falling speed of the item.
            damage (int): The damage the item can inflict.
            points (int): The points awarded when the item is collected.
            width (int): The width of the falling item's rect.
            height (int): The height of the falling item's rect.
            x (int): The initial x-coordinate of the falling item.
            y (int): The initial y-coordinate of the falling item.
            board_instance (Board): An instance of the game board.
        """

        super().__init__(
            name, image, speed, damage, points, width, height, x, y,
            board_instance)

    def disappear(self):

        """
        Handle the disappearance of the points-awarding falling item.
        """

        self.y = 500
        if datetime.datetime.utcnow() > self.stop_time:
            self.y = 500
            self.rect.y = 500
            self.kill()
            self.spawn()
            self.stop_time = (datetime.datetime.utcnow() +
                              datetime.timedelta(seconds=4))


class TickItem(PointsFallingItem, ABC):

    """
    Falling item class representing a Tick that awards 1 point.

    Attributes:
        image (pygame.Surface): The image representing the falling Tick.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):

        """
        Initialises a TickItem object.

        Parameters:
            image (pygame.Surface): The image representing the falling Tick.
            board_instance (Board): An instance of the game board.
        """

        super().__init__(
            "Tick", image, 5, 0, 1, 50, 50, 0, 0, board_instance
        )


class PythonItem(PointsFallingItem, ABC):

    """
    Falling item class representing a Python logo that awards 5 points.

    Attributes:
        image (pygame.Surface): The image representing the falling Python logo.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):

        """
        Initialises a PythonItem object.

        Parameters:
            image (pygame.Surface): The image representing the falling Python logo.
            board_instance (Board): An instance of the game board.
        """

        super().__init__(
            "Python", image, 8, 0, 5, 50, 50, 0, 0, board_instance
        )


class RubberDuckItem(PointsFallingItem, ABC):

    """
    Falling item class representing a Rubber Duck that awards 10 points.

    Attributes:
        image (pygame.Surface): The image representing the falling Rubber Duck.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, image, board_instance):

        """
        Initialises a RubberDuckItem object.

        Parameters:
            image (pygame.Surface): The image representing the falling Rubber Duck.
            board_instance (Board): An instance of the game board.
        """

        super().__init__(
            "Rubber duck", image, 12, 0, 10, 50, 50, 0, 0, board_instance
        )
