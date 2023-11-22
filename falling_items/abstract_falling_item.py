import random
import pygame
from abc import abstractmethod
from abc import ABC


class FallingItem(ABC):
	def __init__(self, name, speed, damage, points, width, height, x, y, board_width):
		self.name = name
		self.speed = speed
		self.damage = damage
		self.points = points
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.board_width = board_width
		self.spawn()

	def spawn(self):
		# self.x = random.randint(0, self.board_width - self.width)
		self.x = 350
		self.y = 0

	def fall(self):
		self.y += self.speed

	@abstractmethod
	def disappear(self):
		pass
	
	@abstractmethod
	def draw(self, board_instance):
		pass