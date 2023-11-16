import pygame
import sys

class Board():
	def __init__(self, name, res, frames):
		self.name = name
		self.res = res
		self.frames = frames

	def display_board(self):
		pygame.init()
		pygame.display.set_caption(self.name)
		board = pygame.display.set_mode(self.res)
		fps = pygame.time.Clock()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fps.tick(self.frames)