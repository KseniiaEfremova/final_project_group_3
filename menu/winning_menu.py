import pygame
from board import Board
from menu.menu import Menu
from models.components.button import Button
from utils import assets_library

pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)


class WinningMenu(Menu):
	def __init__(self, board_instance: Board):
		super().__init__(board_instance)

	def play_again_handler(self):
		print('clicked play again button')

	def exit(self):
		print('played enough for today')

	def draw(self):
		background_image = pygame.image.load(assets_library['backgrounds']['win'])
		image = pygame.transform.scale(background_image, (self.width, self.height))
		text = font.render("Congratulations\n, you won!", True, (255, 255, 255))
		play_again_button = Button(150, 500, 100, 40, self.board_instance, buttonText='Play again', onclickFunction=self.play_again_handler, onePress=True)
		exit_button = Button(350, 500, 100, 40, self.board_instance,
								   buttonText='Exit',
								   onclickFunction=self.exit,
								   onePress=True)
		self.board_instance.board.blit(image, (0, 0))
		self.board_instance.board.blit(text, (150, 425))
		play_again_button.process()
		exit_button.process()



















































































































"""This is work in progress to set fireworks in pygame, will return to it if there is time before launch"""
# import pygame
# import random
# from board import Board
# from menu.menu import Menu
# from models.firework import Firework
# from models.projectile import Projectile
#
# pygame.font.init()
# font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
#
#
# class WinningMenu(Menu):
# 	def __init__(self, board_instance: Board):
# 		super().__init__(board_instance)
# 		self.fireworks = []
# 		self.projectiles = []
# 		self.new_fireworks = True
# 		self.counter = 0
# 		self.directions = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1)]
# 		self.fireworks_to_remove = []
#
# 	def draw(self, **kwargs):
# 		counter = kwargs.get('counter', None)
# 		rect = pygame.Rect(0, 0, self.width, self.height)
# 		win = pygame.Surface((self.width, self.height))
# 		pygame.draw.rect(win, (0, 0, 0, 255), rect)
# 		text = font.render("Congratulations! you won", True, 'white')
# 		if self.new_fireworks:
# 			for _ in range(1, 30):
# 				firework = Firework(self.board_instance)
# 				self.fireworks.append(firework)
# 				self.new_fireworks = False
#
# 			for i in range(len(self.fireworks) - 1):
# 				if (self.fireworks[i].delay < counter and
# 					self.fireworks[i].burst_y_pos < self.fireworks[i].y_pos):
# 					print('drawing')
# 					pygame.draw.rect(win, self.fireworks[i].color, [self.fireworks[i].x_pos, self.fireworks[i].y_pos, 10, 10], 10, 3)
# 					self.fireworks[i].y_pos -= self.fireworks[i].y_speed
# 					self.board_instance.board.blit(win, (0, 0))
# 				elif self.fireworks[i].burst_y_pos >= self.fireworks[i].y_pos:
# 					x_start = self.fireworks[i].x_pos
# 					print(x_start)
# 					y_start = self.fireworks[i].y_pos
# 					print(y_start)
# 					for j in range(len(self.directions)):
# 						projectile = Projectile(x_start, y_start, self.directions[j][0] * 5, self.directions[j][1] * 5, self.fireworks[i].color)
# 						self.projectiles.append(projectile)
# 					self.fireworks_to_remove.append(i)
# 			self.fireworks_to_remove.sort(reverse=True)
# 			for r in self.fireworks_to_remove:
# 				self.fireworks.remove(self.fireworks[r])
# 			self.fireworks_to_remove = []
# 			for i in range(len(self.projectiles)):
# 				color = self.projectiles[i].color[0], self.projectiles[i].color[1], self.projectiles[i].color[2], self.projectiles[i].delay * 4
# 				pygame.draw.circle(win, color, (
# 					self.projectiles[i].x_start, self.projectiles[i].y_start), 3)
# 				self.projectiles[i].delay -= 1
# 				self.projectiles[i].x_start += self.projectiles[i].direction_x
# 				self.projectiles[i].y_start += self.projectiles[i].direction_y
# 				self.projectiles[i].direction_y += 0.1
# 				if self.projectiles[i].delay < 0 or self.board_instance.res[0] < self.projectiles[i].x_start < -3 or self.board_instance.res[1] < self.projectiles[i].y_start:
# 					self.fireworks_to_remove.append(i)
# 				for p in range(len(self.fireworks_to_remove)):
# 					self.projectiles.pop(0)
#
# 		if len(self.fireworks) == 0 and len(self.projectiles) == 0:
# 			self.new_fireworks = True
#
# 		self.board_instance.board.blit(win, (0, 0))
# 		self.board_instance.board.blit(text, (150, 225))

