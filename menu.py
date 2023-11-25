import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font('assets/Kiddy Play.ttf', 40)


class Menu:
	def __init__(self, board_instance: Board):
		self.board_instance = board_instance
		self.x = 0
		self.y = 0

	def draw(self):
		pause = pygame.Rect(0, 0, 800, 600)
		pygame.draw.rect(self.board_instance.board_surface, (128, 128, 128, 150), pause)
		text = font.render("Game paused", True, (255, 255, 255))
		self.board_instance.board.blit(text, (325, 275))
