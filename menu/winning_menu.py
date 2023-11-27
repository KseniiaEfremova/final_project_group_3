import pygame
from board import Board
from menu.menu import Menu

pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)

class WinningMenu(Menu):
	def __init__(self, board_instance: Board):
		super().__init__(board_instance)
		self.fireworks = []
		self.projectile = []
		self.new_fireworks = True
		self.counter = 0
		self.colors = [(255, 0, 0), (0, 0, 255), (255, 255, 255)]
