from abc import ABC
import pygame
from stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 40)


class Timer(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__(player_instance, board_instance)
		self.x = 10
		self.y = 75

	def update(self):
		pass

	def draw(self, board_instance, **kwargs):
		timer = kwargs.get('timer', None)
		if timer is not None:
			text = font.render(f"Time: {timer}", True, (255, 255, 255))
			self.board_instance.board.blit(text, (20, 20))
