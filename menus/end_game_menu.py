import pygame
import sys
from board import Board
from menus.menu import Menu
from models.components.button import Button
from utils import assets_library


pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)


class EndGameMenu(Menu):
	def __init__(self, board_instance: Board, background_pic, text=None):
		super().__init__(board_instance)
		self.play_again = False
		self.background_pic = background_pic
		self.text = text

	def get_play_again(self):
		return self.play_again

	def play_again_handler(self):
		self.play_again = True

	def exit_game_handler(self):
		pygame.quit()
		sys.exit()

	def draw(self):
		background_image = pygame.image.load(self.background_pic)
		image = pygame.transform.scale(background_image, (self.width, self.height))
		if self.text is not None:
			text = font.render(self.text, True, (255, 255, 255))
			self.board_instance.board.blit(text, (220, 400))
		play_again_button = Button(200, 500, 150, 40, self.board_instance, buttonText='Play again', onclickFunction=self.play_again_handler, onePress=False)
		exit_button = Button(450, 500, 150, 40, self.board_instance,
								   buttonText='Exit',
								   onclickFunction=self.exit_game_handler,
								   onePress=False)
		self.board_instance.board.blit(image, (0, 0))

		play_again_button.process()
		exit_button.process()
