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
    def __init__(self, board_instance: Board, history=True):
        super().__init__(board_instance)
        self.history = history
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


    def exit_game_handler(self):
        pygame.quit()
        sys.exit()


    def draw(self):
        player_data = self.get_history_data()
        self.board_instance.draw_background()
        self.text_drawer.draw_text("HISTORY", (255, 255, 255), 100, 180, font)

        # Draw column names
        x = 50
        y = 100
        for col_name in self.column_names:
            self.text_drawer.draw_text(col_name, (255, 255, 255), x, y, font)
            x += 150

        # Draw data
        y += 50
        for row in player_data:
            x = 50
            for value in row:
                self.text_drawer.draw_text(str(value), (255, 255, 255), x, y, font)
                x += 150
            y += 30

        self.exit_button.process()
        pygame.display.update()
        
        
    def process_history(self):
        self.board_instance.image = pygame.transform.scale(self.background_image, (800, 600))
        self.draw()
        self.history = False
