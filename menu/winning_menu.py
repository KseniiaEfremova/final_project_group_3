import pygame
import random
from board import Board
from menu.menu import Menu
from models.firework import Firework
from models.projectile import Projectile

pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)


class WinningMenu(Menu):
	def __init__(self, board_instance: Board):
		super().__init__(board_instance)
		self.fireworks = []
		self.projectiles = []
		self.new_fireworks = True
		self.counter = 0
		self.directions = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1)]

	def draw(self):
		if self.new_fireworks:
			for _ in range(1, 30):
				firework = Firework(self.board_instance)
				self.fireworks.append(firework)
				self.new_fireworks = False


				for i in range(len(self.fireworks) - 1):
					if (self.fireworks[i]['delay'] < self.counter and
							self.fireworks[i]['burst_y_pos'] < self.fireworks[i]['y_pos']):
						pygame.draw.rect(self.board_instance.board_surface, self.fireworks[i]['color'], [self.fireworks[i]['x_pos'], self.fireworks[i]['y_pos'],10, 10], 0, 3 )
						self.fireworks[i]['y_pos'] -= self.fireworks[i]['y_speed']
					elif self.fireworks[i]['burst_y_pos'] >= self.fireworks[i]['y_pos']:
						x_start = self.fireworks[i]['x_pos']
						y_start = self.fireworks[i]['y_pos']
						for j in range(len(self.directions)):
							projectile = Projectile(x_start, y_start, self.directions[j][0] * 5, self.directions[j][1] * 5, self.fireworks[i]['color'])
							self.projectiles.append(projectile)

				if len(self.fireworks) == 0 and len(self.projectiles) == 0:
					self.counter = 0
					self.new_fireworks = True
