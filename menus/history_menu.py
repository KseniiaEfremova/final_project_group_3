import pygame
import sys
from menus.menu import Menu
from db_utils import get_cursor_and_connection
from board import Board
from models.components.button import Button
from models.components.text_drawer import TextDrawer
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class HistoryMenu(Menu):
    """ Represents the history menu for users to see their stats"""
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.history = True
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.text_drawer = TextDrawer(self.board_instance)
        self.exit_button = Button(450, 500, 150, 40, self.board_instance, buttonText='Exit', onclickFunction=self.exit_game_handler, onePress=False)
        self.column_names = ["Username", "Points", "Life", "Level"]

    def get_history_data(self):
        cursor, db_connection = get_cursor_and_connection("game_users_db")
        try:
            query = """SELECT u.username, g.points, g.life, g.level
                       FROM users AS u
                       JOIN game_statistics AS g ON u.user_id = g.user_id
                       ORDER BY g.level DESC, g.points DESC
                       LIMIT 8
                    """
            cursor.execute(query)
            return cursor.fetchall()
        
        finally:
            cursor.close()
            db_connection.close()

        
    def get_play_again(self):
        return self.play_again
    
    
    def play_again_handler(self):
        self.play_again = True
        
        
    def exit_game_handler(self):
        pygame.quit()
        sys.exit()
        
        
    def draw(self):
        player_data = self.get_history_data()
        background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))

        # Draw title
        title_text = font.render("HISTORY", True, (255, 255, 255))
        self.board_instance.board.blit(title_text, (150, 200))

        # Draw column names
        column_x = 150
        column_y = 250
        for col_name in self.column_names:
            col_text = font.render(col_name, True, (255, 255, 255))
            self.board_instance.board.blit(col_text, (column_x, column_y))
            column_x += 150

        # Draw data
        data_y = 300
        for row in player_data:
            data_x = 150
            for value in row:
                value_text = font.render(str(value), True, (255, 255, 255))
                self.board_instance.board.blit(value_text, (data_x, data_y))
                data_x += 150
            data_y += 30

        play_button = Button(200, 500, 150, 40, self.board_instance, buttonText='Play', onclickFunction=self.play_again_handler, onePress=False)
        exit_button = Button(450, 500, 150, 40, self.board_instance, buttonText='Exit', onclickFunction=self.exit_game_handler, onePress=False)
        play_button.process()
        exit_button.process()

        pygame.display.update()
        self.history = False
