import pygame
from board import Board
from menus.menu import Menu
import sys
from models.components.button import Button

pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)

class GameOverMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.restart_game = False

    def get_restart_game(self):
        print("Restart Game Handler Called")
        return self.restart_game

    def restart_game_handler(self):
        self.restart_game = True

    def exit_game_handler(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        background_image = pygame.image.load('assets/backgrounds/game_over.png')
        image = pygame.transform.scale(background_image, (self.width, self.height))
       # text = font.render("Game Over", True, (255, 255, 255))
        restart_game_button = Button(200, 500, 150, 40, self.board_instance, buttonText='Play again',
                                   onclickFunction=self.restart_game_handler, onePress=False)
        exit_game_button = Button(450, 500, 150, 40, self.board_instance,
                             buttonText='Exit',
                             onclickFunction=self.exit_game_handler,
                             onePress=False)
        self.board_instance.board.blit(image, (0, 0))
        #self.board_instance.board.blit(text, (220, 400))
        restart_game_button.process()
        exit_game_button.process()


    #def __init__(self, board_instance: Board, player: Player):
    #    super().__init__(board_instance)
    #    pygame.font.init()
    #    self.player = player
    #    self.font_game_over = pygame.font.Font('assets/fonts/FukuCatch.otf', 60)
    #    self.font_play_again_exit = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)

    #def draw_button(self, surface, text, font, color, x, y, width, height, hover=False):
    #    pygame.draw.rect(surface, color, (x, y, width, height), border_radius=10)
    #    text_render = font.render(text, True, (255, 255, 255))
    #    surface.blit(text_render, (x + width // 2 - text_render.get_width() // 2, y + height // 2 - text_render.get_height() // 2))


    #def draw(self):
    #    over = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
    #    self.game_over_image(self.board_instance)


    #    center_x = self.width // 2
    #    center_y = self.height // 2


    #    play_again_width = 250
    #    play_again_height = 40
    #    play_again_x = center_x - play_again_width - 10
    #    play_again_y = center_y + 200

    #    play_again_rect = pygame.Rect(play_again_x, play_again_y, play_again_width, play_again_height)
    #    play_again_hovered= play_again_rect.collidepoint(pygame.mouse.get_pos())
    #    play_again_color = (255, 192, 203) if not play_again_hovered else (255, 160, 180)
    #    self.draw_button(over, "Play Again", self.font_play_again_exit, play_again_color, play_again_x,
    #                     play_again_y, play_again_width, play_again_height, hover=play_again_hovered)



    #    exit_width = 250
    #    exit_height = 40
    #    exit_x = center_x + 10
    #    exit_y = center_y + 200
    #    exit_rect = pygame.Rect(exit_x, exit_y, exit_width, exit_height)
    #    exit_hovered = exit_rect.collidepoint(pygame.mouse.get_pos())
    #    exit_color = (255, 192, 203) if not exit_hovered else (255, 160, 180)
    #    self.draw_button(over, "Exit", self.font_play_again_exit, exit_color, exit_x, exit_y, exit_width,
    #                 exit_height, hover=exit_hovered)


    #    self.board_instance.board.blit(over, (0, 0))

    #def game_over_image(self, board_instance):
    #    game_over_image = pygame.image.load('assets/backgrounds/game_over.png')
    #    game_over_image = pygame.transform.scale(game_over_image, (600, 600))
    #    board_instance.board.blit(game_over_image, (60, 0))

    #def handle_events(self):
    #    for event in pygame.event.get():
    #        if event.type == pygame.MOUSEBUTTONDOWN:
    #            x, y = pygame.mouse.get_pos()
    #            play_again_rect = pygame.Rect(self.width // 2 - 260, self.height // 2 + 200, 250, 40)
    #            exit_rect = pygame.Rect(self.width // 2 + 10, self.height // 2 + 200, 250, 40)

    #            if play_again_rect.collidepoint(x, y):
    #                self.player.reset_player_stats()
    #                self.board_instance.over = False
    #                self.board_instance.pause = False
    #                self.board_instance.display_board()
    #            elif exit_rect.collidepoint(x, y):
    #                pygame.quit()
    #                sys.exit()























