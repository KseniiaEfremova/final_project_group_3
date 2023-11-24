from abc import ABC
import pygame
from stats.abstract_stats import Stats
from player import Player
from board import Board


class Level(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__(player_instance, board_instance)
		self.sprites = []
		self.player_instance = player_instance
		self.level = self.player_instance.level - 1
		self.sprites.append(pygame.image.load("assets/level1.png"))
		self.sprites.append(pygame.image.load("assets/level2.png"))
		self.sprites.append(pygame.image.load("assets/level3.png"))
		self.current_sprite = self.level
		self.width = 70
		self.height = 70
		self.x = 500
		self.y = 75
		self.image = pygame.transform.scale(self.sprites[self.current_sprite],
											(self.width, self.height))
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.board_instance = board_instance

	def update(self):
		self.current_sprite = self.level
		if self.current_sprite > 2:
			print('you won! game is over, wanna play again?')
			self.current_sprite = 2

	def draw(self, board_instance, **kwargs):
		self.update()
		board_instance.board.blit(self.image, (self.x - self.width,
											   self.y - self.height))


