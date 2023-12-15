import pygame
import sys
from menus.menu import Menu
from db.history import get_history_data
from board import Board
from models.components.button import Button
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 20)


class HistoryMenu(Menu):
    """ Represents the history menu for users to see their stats"""
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.history = True
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.column_names = ["Username", "Points", "Life", "Level"]
        self.back_btn = Button(20, 550, 200, 40, self.board_instance, 'BACK TO MENU',
                               self.back_button_handler)

        
    def get_play_again(self):
        return self.play_again
    
    
    def play_again_handler(self):
        self.play_again = True
        
        
    def exit_game_handler(self):
        pygame.quit()
        sys.exit()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.back_button_handler()

    def back_button_handler(self):
        self.history = False
        
    def draw(self):
        player_data = get_history_data()
        background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        self.back_btn.process()

        # Draw title
        title_text = font.render("HISTORY", True, (255, 255, 255))
        self.board_instance.board.blit(title_text, (350, 180))

        # Draw column names
        column_x = 100
        column_y = 230
        for col_name in self.column_names:
            col_text = font.render(col_name, True, (255, 255, 255))
            self.board_instance.board.blit(col_text, (column_x, column_y))
            column_x += 190

        # Draw data
        data_y = 270
        for row in player_data:
            data_x = 100
            for value in row:
                value_text = font.render(str(value), True, (255, 255, 255))
                self.board_instance.board.blit(value_text, (data_x, data_y))
                data_x += 190
            data_y += 30

        # play_button = Button(200, 550, 150, 40, self.board_instance, buttonText='Play', onclickFunction=self.play_again_handler, onePress=False)
        # exit_button = Button(450, 550, 150, 40, self.board_instance, buttonText='Exit', onclickFunction=self.exit_game_handler, onePress=False)
        # play_button.process()
        # exit_button.process()

        pygame.display.update()
