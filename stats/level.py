from abc import ABC
import pygame
from stats.abstract_stats import Stats
from models.player import Player
from board import Board
from utils import assets_library


class Level(Stats, ABC):
	def __init__(self, player_instance: Player, board_instance: Board):
		super().__init__(player_instance, board_instance)
		self.sprites = []
		self.level = self.player_instance.level - 1
		self.sprites.append(pygame.image.load(assets_library['sprites']['level']['level1']))
		self.sprites.append(pygame.image.load(assets_library['sprites']['level']['level2']))
		self.sprites.append(pygame.image.load(assets_library['sprites']['level']['level3']))
		self.current_sprite = self.level
		self.width = 70
		self.height = 70
		self.x = 550
		self.y = 75
		self.image = pygame.transform.scale(self.sprites[self.current_sprite],
											(self.width, self.height))
		self.rect = pygame.Rect(0, 0, self.width, self.height)

	def update(self):
		self.current_sprite = self.player_instance.get_level()
		if self.current_sprite > 2:
			# display winning screen
			print('you won! game is over, wanna play again?')
			self.current_sprite = 2

	def draw(self, board_instance, **kwargs):
		self.update()
		board_instance.board.blit(self.image, (self.x - self.width,
											   self.y - self.height))

	def display_level_up_image(self, board_instance):
		level_up_image = pygame.image.load(assets_library['backgrounds']['level_up'])
		level_up_image = pygame.transform.scale(level_up_image, (600, 600))
		board_instance.board.blit(level_up_image, (100, 0))
		pygame.display.update()
		pygame.time.delay(2000) 

