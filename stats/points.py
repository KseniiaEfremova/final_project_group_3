from abc import ABC
import pygame
from stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 40)


class Points(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__(player_instance, board_instance)
		self.x = 500
		self.y = 75
		self.points = player_instance.points

	def update(self):
		pass

	def draw(self, board_instance, **kwargs):
		text = font.render(f"Points: {self.points}", True, (255, 255, 255))
		self.board_instance.board.blit(text, (170, 20))
