import random
from abc import abstractmethod
from abc import ABC
import pygame
import datetime
from board import Board


class FallingItem(ABC, pygame.sprite.Sprite):
    """
    Abstract base class for falling items in Code Quest.

    Attributes:
        name (str): The name of the falling item.
        image (pygame.Surface): The image representing the falling item.
        speed (int): The speed at which the falling item descends.
        damage (int): The damage inflicted by the falling item.
        points (int): The points awarded for catching the falling item.
        width (int): The width of the falling item.
        height (int): The height of the falling item.
        x (int): The x-coordinate of the falling item's current position.
        y (int): The y-coordinate of the falling item's current position.
        rect (pygame.Rect): The rectangular area occupied by the falling item.
        board_instance (Board): An instance of the game board.
        stop_time (datetime.datetime): The time at which the falling item stops spawning.
    """
    
    def __init__(self, name, image, speed, damage, points, width, height, x, y,
				board_instance: Board):
        """
        Initialises a FallingItem object.

        Parameters:
            name (str): The name of the falling item.
            image (pygame.Surface): The image representing the falling item.
            speed (int): The speed at which the falling item descends.
            damage (int): The damage inflicted by the falling item.
            points (int): The points awarded for catching the falling item.
            width (int): The width of the falling item.
            height (int): The height of the falling item.
            x (int): The x-coordinate of the falling item's initial position.
            y (int): The y-coordinate of the falling item's initial position.
            board_instance (Board): An instance of the game board.
        """
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.speed = speed
        self.damage = damage
        self.points = points
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.board_instance = board_instance
        self.stop_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=3)
        self.spawn()
        
    def spawn(self):
        """
        Spawn the falling item at a random position.

        Returns:
            tuple: The x and y coordinates of the spawned falling item.
        """
        self.x = random.randint(0, 770)
        self.y = random.randint(-400, -100)
        self.rect.x = self.x
        self.rect.y = self.y
        return self.x, self.y
    
    @abstractmethod
    def disappear(self):
        """
        Abstract method to handle the disappearance of the falling item.
        """
        pass
    
    def fall(self):
        """
        Move the falling item down the screen.
        """
        self.y += self.speed
        self.rect.y = self.y
        if self.y > 500:
            self.disappear()
    
    def draw(self, board_instance):
        """
        Draw the falling item on the game board.

        Parameters:
            board_instance (Board): An instance of the game board.
        """
        board_instance.board.blit(self.image, (self.x - self.width,
											   self.y - self.height))
