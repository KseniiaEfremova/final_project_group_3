from abc import ABC
import pygame
from stats.abstract_stats import Stats
from player import Player
from board import Board

pygame.font.init()
font = pygame.font.Font('assets/Kiddy Play.ttf', 40)


class Points(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__(player_instance, board_instance)
		self.player_instance = player_instance
		self.board_instance = board_instance
		self.x = 500
		self.y = 75
		self.points = player_instance.points

	def update(self):
		pass

	def draw(self, board_instance, **kwargs):
		points_rect = pygame.Rect(70, 10, 111, 45)
		pygame.draw.rect(board_instance.board_surface, (0, 0, 0, 0), points_rect)
		text = font.render("Points: {}".format(self.points), True, (255, 255, 255))
		self.board_instance.board.blit(text, (170, 20))
