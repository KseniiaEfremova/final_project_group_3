from abc import abstractmethod
from abc import ABC
import pygame
from board import Board
from models.player import Player


class Stats(ABC, pygame.sprite.Sprite):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__()
		self.board_instance = board_instance
		self.player_instance = player_instance

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def draw(self, board_instance, *args, **kwargs):
		pass
