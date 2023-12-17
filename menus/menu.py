from abc import abstractmethod
from abc import ABC
import pygame
import sys
from board import Board


class Menu(ABC):

	"""
	Abstract base class representing a menu in the game.

	Attributes:
		board_instance (Board): An instance of the Board class associated with
		the menu.
		width (int): Width of the menu, obtained from the Board instance.
		height (int): Height of the menu, obtained from the Board instance.
	"""

	def __init__(self, board_instance: Board):

		"""
		Initialise a Menu instance.

		Args:
			board_instance (Board): An instance of the Board class associated
			with the menu.
		"""

		super().__init__()
		self.board_instance = board_instance
		self.width = board_instance.res[0]
		self.height = board_instance.res[1]

	@abstractmethod
	def draw(self, **kwargs):

		"""
		Abstract method for drawing the menu on the board.

		This method must be implemented by subclasses to define how the menu is
		drawn.

		Args:
			**kwargs: Additional keyword arguments that subclasses might use for
			drawing.
		"""

		pass

	def back_button_handler(self):

		"""
		Handles state changes in opening menus.
		"""

		pass

	def event_handler(self):

		"""
		Method for handling quit and mouse events.
		"""

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.back_button_handler()
