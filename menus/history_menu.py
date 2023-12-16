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
    def __init__(self, board_instance: Board):
        """
        Initialise the HistoryMenu.

        Args:
            board_instance (Board): The game board instance.
        """
        super().__init__(board_instance)
        self.history = True
        self.background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        self.column_names = ["Username", "Points", "Life", "Level"]
        self.back_btn = Button(
            0, 560, 190, 40, self.board_instance,
            'BACK TO MENU', self.back_button_handler)

    def get_play_again(self):
        """
        Get the play_again status.

        Returns:
            bool: The play_again status.
        """
        return self.play_again

    def play_again_handler(self):
        """
        Handle the play again action.

        Set the play_again flag to True.
        """
        self.play_again = True

    def exit_game_handler(self):
        """
        Handle the exit game action.

        Quit the pygame application and exit the system.
        """
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

    def draw_columns(self, surface):
        """
          Draw 4 columns based on column_names list.

          Display text on the surface.
        """
        column_x = 100
        column_y = 230
        for col_name in self.column_names:
            col_text = font.render(
                col_name, True, (255, 255, 255))
            surface.blit(col_text, (column_x, column_y))
            column_x += 190

    def draw_rows(self, surface):
        """
          Draw 8 rows based on history_data from db.

          Display text on the surface.
        """
        player_data = get_history_data()
        data_y = 270
        for row in player_data:
            data_x = 100
            for value in row:
                value_text = font.render(
                    str(value), True, (255, 255, 255))
                surface.blit(value_text, (data_x, data_y))
                data_x += 190
            data_y += 30

    def draw(self):
        """
        Draw the history menu on the board.

        Display the background image, title, column names, data and button.
        """

        background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(
            background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        self.back_btn.process()

        title_text = font.render(
            "HISTORY", True, (255, 255, 255))
        self.board_instance.board.blit(title_text, (350, 180))

        self.draw_columns(self.board_instance.board)
        self.draw_rows(self.board_instance.board)
        pygame.display.update()
