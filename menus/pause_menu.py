import pygame
from board import Board
from menus.menu import Menu
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['fuku_catch'], 60)


class PauseMenu(Menu):
	def __init__(self, board_instance: Board):
		super().__init__(board_instance)

	def draw(self):
		rect = pygame.Rect(0, 0, self.width, self.height)
		pause = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		pygame.draw.rect(pause, (135, 135, 135, 150), rect)
		text = font.render("Game paused", True, (255, 255, 255))
		self.board_instance.board.blit(pause, (0, 0))
		self.board_instance.board.blit(text, (150, 225))
