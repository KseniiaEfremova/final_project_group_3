import pygame
from board import Board
from menus.menu import Menu
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['fuku_catch'], 60)


class PauseMenu(Menu):
	"""
	Represents the menu displayed when the game is paused.

    Attributes:
        board_instance (Board): An instance of the Board class associated with the pause menu.
        width (int): Width of the pause menu.
        height (int): Height of the pause menu.
	"""

	def __init__(self, board_instance: Board):
		"""
		Initialise a PauseMenu instance.

        Args:
            board_instance (Board): An instance of the Board class associated with the pause menu.
		"""
		super().__init__(board_instance)

	def draw(self):
		"""
		Draw the pause menu on the board.
		"""
		rect = pygame.Rect(0, 0, self.width, self.height)
		pause = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		pygame.draw.rect(pause, (135, 135, 135, 150), rect)
		text = font.render("Game paused", True, (255, 255, 255))
		self.board_instance.board.blit(pause, (0, 0))
		self.board_instance.board.blit(text, (150, 225))
