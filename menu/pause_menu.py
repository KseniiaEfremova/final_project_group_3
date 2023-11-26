import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font('assets/Kiddy Play.ttf', 40)


class PauseMenu:
	def __init__(self, board_instance: Board):
		self.board_instance = board_instance
		self.width = board_instance.res[0]
		self.height = board_instance.res[1]

	def draw(self):
		rect = pygame.Rect(0, 0, self.width, self.height)
		pause = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		pygame.draw.rect(pause, (135, 135, 135, 150), rect)
		text = font.render("Game paused", True, (255, 255, 255))
		self.board_instance.board.blit(pause, (0, 0))
		self.board_instance.board.blit(text, (325, 275))
