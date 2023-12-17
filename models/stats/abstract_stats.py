from abc import abstractmethod
from abc import ABC
import pygame
from board import Board
from models.player import Player


class Stats(ABC, pygame.sprite.Sprite):

    """
    Abstract base class for representing player stats in Code Quest.

    Attributes:
        player_instance (Player): An instance of the player associated with the stats.
        board_instance (Board): An instance of the game board.
    """
    
    def __init__(self, player_instance: Player, board_instance: Board):

        """
        Initialise a Stats object.

        Parameters:
            player_instance (Player): An instance of the player associated with the stats.
            board_instance (Board): An instance of the game board.
        """

        super().__init__()
        self.board_instance = board_instance
        self.player_instance = player_instance
        
    @abstractmethod
    def update(self):

        """
        Abstract method to update the stats.
        """

        pass
    
    @abstractmethod
    def draw(self, board_instance, *args, **kwargs):

        """
        Abstract method to draw the stats on the game board.

        Parameters:
            board_instance (Board): An instance of the game board.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """

        pass
