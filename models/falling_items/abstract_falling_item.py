import random
from abc import abstractmethod
from abc import ABC
import pygame
import datetime
from board import Board
from decorators.sounds import Sounds


long_stop = datetime.datetime.utcnow() + datetime.timedelta(
	seconds=3)
medium_stop = datetime.datetime.utcnow() + datetime.timedelta(
	seconds=2)
short_stop = datetime.datetime.utcnow() + datetime.timedelta(
	seconds=1)


class FallingItem(ABC, pygame.sprite.Sprite):
	def __init__(self, name, image, speed, damage, points, width, height, x, y,
				board_instance: Board):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		self.image = image
		self.speed = speed
		self.damage = damage
		self.points = points
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)
		self.board_instance = board_instance
		self.spawn()

	def spawn(self):
		self.x = random.randint(0, 770)
		self.y = random.randint(-500, -100)
		self.rect.x = self.x
		self.rect.y = self.y

	@abstractmethod
	def disappear(self, stop_time):
		pass

	def fall(self):
		self.y += self.speed
		self.rect.y = self.y

	def draw(self, board_instance):
		board_instance.board.blit(self.image, (self.x - self.width,
											   self.y - self.height))


