import pygame
from board import Board
from menu.menu import Menu

#pygame.font.init()
#font_game_over = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
#font_play_again_exit = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)

class GameOverMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        pygame.font.init()
        self.font_game_over = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
        self.font_play_again_exit = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)

    def draw_button(self, surface, text, font, color, x, y, width, height):
        pygame.draw.rect(surface, color, (x, y, width, height), border_radius=10)
        text_render = font.render(text, True, (255, 255, 255))
        surface.blit(text_render, (x + width // 2 - text_render.get_width() // 2, y + height // 2 - text_render.get_height() // 2))

    def draw(self):
        rect = pygame.Rect(0, 0, self.width, self.height)
        game_over_menu = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(game_over_menu, (135, 135, 135, 150), rect)

        text_game_over = self.font_game_over.render("Game Over", True, (255, 255, 255))
        center_x = self.width // 2
        center_y = self.height // 2
        game_over_menu.blit(text_game_over, (center_x - text_game_over.get_width() // 2, center_y - 50))


        play_again_width = 250
        play_again_height = 40
        play_again_x = center_x - play_again_width // 2
        play_again_y = center_y + 16
        self.draw_button(game_over_menu, "Play Again", self.font_play_again_exit, (255, 192, 203), play_again_x, play_again_y, play_again_width, play_again_height)


        exit_width = 250
        exit_height = 40
        exit_x = center_x - exit_width // 2
        exit_y = center_y + 65
        self.draw_button(game_over_menu, "Exit", self.font_play_again_exit, (255, 192, 203), exit_x, exit_y, exit_width, exit_height)

        self.board_instance.board.blit(game_over_menu, (0, 0))












#class GameOverMenu(Menu):
#	def __init__(self, board_instance: Board):
#		super().__init__(board_instance)
#	pygame.font.init()
#	font_game_over = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
#	font_play_again_exit = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)

#	def draw(self):
#		rect = pygame.Rect(0, 0, self.width, self.height)
#		game_over_menu = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
#		pygame.draw.rect(game_over_menu, (135, 135, 135, 150), rect)
#		text_game_over = font_game_over.render("Game Over", True, (255, 255, 255))
#		text_play_again = font_play_again_exit.render("Play Again", True, (255, 255, 255))
#		text_exit = font_play_again_exit.render("Exit", True, (255, 255, 255))

#		center_x = self.width // 2
#		center_y = self.height // 2

#		game_over_menu.blit(text_game_over, (center_x - text_game_over.get_width() // 2, center_y - 50))
#		game_over_menu.blit(text_play_again, (center_x - text_play_again.get_width() // 2, center_y + 16))
#		game_over_menu.blit(text_exit, (center_x - text_exit.get_width() // 2, center_y + 50))

#		self.board_instance.board.blit(game_over_menu, (0, 0))



#def is_play_again_clicked(self, mouse_pos):
#		print("Play Again Clicked at:", mouse_pos)
#		return 150 <= mouse_pos[0] <= 235 and 346 <= mouse_pos[1] <= 350

#	def is_exit_clicked(self, mouse_pos):
#		print("Exit Clicked at:", mouse_pos)
#		return 150 <= mouse_pos[0] <= 350 and 400 <= mouse_pos[1] <= 450









