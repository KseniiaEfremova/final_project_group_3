from abc import abstractmethod
from abc import ABC


class FallingItem(ABC):
	def __init__(self, name, speed, damage, points, width, height, x, y):
		self.name = name
		self.speed = speed
		self.damage = damage
		self.points = points
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@abstractmethod
	def spawn(self):
		pass

	@abstractmethod
	def fall(self):
		pass

	@abstractmethod
	def disappear(self):
		pass
	
	@abstractmethod
	def draw(self, board_instance):
		pass
