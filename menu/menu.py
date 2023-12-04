import pygame
from abc import abstractmethod
from abc import ABC
from board import Board


class Menu(ABC):
	def __init__(self, board_instance: Board):
		super().__init__()
		self.board_instance = board_instance
		self.width = board_instance.res[0]
		self.height = board_instance.res[1]

	@abstractmethod
	def draw(self, **kwargs):
		pass
