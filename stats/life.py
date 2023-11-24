from abc import ABC
import pygame
from stats.abstract_stats import Stats
from player import Player
from board import Board


class Life(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board, width, height):
		super().__init__(player_instance, board_instance, width, height)
		self.sprites = []
		self.player_instance = player_instance
		self.lives = self.player_instance.life
		self.sprites.append(pygame.image.load("assets/heart_full.png"))
		self.sprites.append(pygame.image.load("assets/heart_almost_full.png"))
		self.sprites.append(pygame.image.load("assets/heart_medium2.png"))
		self.sprites.append(pygame.image.load("assets/heart_medium1.png"))
		self.sprites.append(pygame.image.load("assets/heart_low.png"))
		self.sprites.append(pygame.image.load("assets/heart_empty.png"))
		self.current_sprite = 0
		self.x_positions = [725, 665, 605]
		self.images = []
		self.width = 50
		self.height = 50
		self.y = 75
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.board_instance = board_instance
		self.spawn()

	def spawn(self):
		for x_pos in self.x_positions:
			image = pygame.transform.scale(self.sprites[self.current_sprite],
										   (50, 50))
			self.images.append(image)

	def update(self):
		pass

	def draw(self, board_instance):
		for index, image in enumerate(self.images):
			x = self.x_positions[index]
			board_instance.board.blit(image, (x, self.y - self.height))