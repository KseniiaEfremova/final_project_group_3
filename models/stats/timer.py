from abc import ABC
import pygame
from models.stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 40)


class Timer(Stats, ABC):
	"""
    Class representing the Timer in Code Quest.

    Attributes:
        player_instance (Player): An instance of the player associated with the timer.
        board_instance (Board): An instance of the game board.
        x (int): The x-coordinate for displaying the timer on the game board.
        y (int): The y-coordinate for displaying the timer on the game board.
	"""
    
	def __init__(self, player_instance: Player, board_instance: Board):
		"""
        Initialise a Timer object.

        Parameters:
            player_instance (Player): An instance of the player associated with the timer.
            board_instance (Board): An instance of the game board.
		"""
		super().__init__(player_instance, board_instance)
		self.x = 10
		self.y = 75

	def update(self):
		"""
        Update the Timer.

        Returns:
            None
		"""
		pass

	def draw(self, board_instance, **kwargs):
		"""
        Draw the Timer on the game board.

        Parameters:
            board_instance (Board): An instance of the game board.
            **kwargs: Additional keyword arguments.
		"""
		timer = kwargs.get('timer', None)
		if timer is not None:
			text = font.render(
				f"Time: {timer}", True, (255, 255, 255))
			self.board_instance.board.blit(text, (20, 20))
