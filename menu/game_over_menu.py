import pygame
from board import Board
from menu.menu import Menu


pygame.font.init()
font_game_over = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
font_play_again_exit = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)


class GameOverMenu(Menu):
	def __init__(self, board_instance: Board):
		super().__init__(board_instance)

	def draw(self):
		rect = pygame.Rect(0, 0, self.width, self.height)
		game_over_menu = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		pygame.draw.rect(game_over_menu, (135, 135, 135, 150), rect)
		text_game_over = font_game_over.render("Game Over", True, (255, 255, 255))
		text_play_again = font_play_again_exit.render("Play Again", True, (255, 255, 255))
		text_exit = font_play_again_exit.render("Exit", True, (255, 255, 255))

		center_x = self.width // 2
		center_y = self.height // 2

		game_over_menu.blit(text_game_over, (center_x - text_game_over.get_width() // 2, center_y - 50))
		game_over_menu.blit(text_play_again, (center_x - text_play_again.get_width() // 2 , center_y + 16))
		game_over_menu.blit(text_exit, (center_x - text_exit.get_width() // 2 , center_y + 50))

		self.board_instance.board.blit(game_over_menu, (0, 0))










