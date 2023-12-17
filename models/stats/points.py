from abc import ABC
import pygame
from models.stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 40)


class Points(Stats, ABC):

	"""
	Class representing the player's Points in Code Quest.

	Attributes:
		player_instance (Player): An instance of the player associated with the
		points.
		board_instance (Board): An instance of the game board.
		x (int): The x-coordinate for displaying the points on the game board.
		y (int): The y-coordinate for displaying the points on the game board.
		points (int): The current number of points of the player.
	"""

	def __init__(self, player_instance: Player, board_instance: Board):

		"""
		Initialise a Points object.

		Parameters:
			player_instance (Player): An instance of the player associated with
			the points.
			board_instance (Board): An instance of the game board.
		"""

		super().__init__(player_instance, board_instance)
		self.x = 500
		self.y = 75
		self.points = self.player_instance.get_points()

	def update(self):

		"""
		Update the current number of points based on the player's points.

		Returns:
			None
		"""

		self.points = self.player_instance.get_points()

	def draw(self, board_instance, **kwargs):

		"""
		Draw the player's points on the game board.

		Parameters:
			board_instance (Board): An instance of the game board.
			**kwargs: Additional keyword arguments.
		"""

		self.update()
		text = font.render(
			f"Points: {self.points}", True,
			(255, 255, 255))
		self.board_instance.board.blit(text, (170, 20))
