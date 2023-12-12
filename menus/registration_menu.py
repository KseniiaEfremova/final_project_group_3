import pygame
from models.components.popup import PopupWindow
from db.user import check_username_and_password, is_user_exist_in_db, add_valid_user_data_to_db, DB_NAME, users_table
from board import Board
from models.components.button import Button
from models.components.input_box import InputBox
from menus.menu import Menu
from models.components.text_drawer import TextDrawer
from utils import assets_library
from pygame.locals import *

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class RegistrationMenu(Menu):
    """
    Represents the registration menu for user sign-up.

    Attributes:
    - board_instance (Board): The instance of the game board.
    - registration (bool): Flag indicating whether it's a registration or login menu.
    - background_image (pygame.Surface): The background image for the registration page.
    - username_box (InputBox): Input box for entering the username.
    - password_box (InputBox): Input box for entering the password.
    - text_drawer (TextDrawer): Helper class for drawing text on the board.
    - submit_btn (Button): Button for submitting the registration or login information.
    - popup_window_invalid (PopupWindow): Popup window for invalid input.
    - popup_window_exist (PopupWindow): Popup window for an existing username.
    """

    def __init__(self, board_instance: Board, registration=True):
        super().__init__(board_instance)
        self.registration = registration
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.username_box = InputBox(250, 250, 140, 32, "", self.board_instance)
        self.password_box = InputBox(250, 350, 140, 32, "", self.board_instance)
        self.text_drawer = TextDrawer(self.board_instance)
        self.submit_btn = Button(300, 420, 200, 40, self.board_instance, 'SUBMIT',
                                 lambda: check_username_and_password(self.username_box.get_user_text(),
                                                                     self.password_box.get_user_text()))

        self.popup_window_invalid = PopupWindow(800, 40, "Invalid Username or Password!")
        self.popup_window_exist = PopupWindow(800, 40, "This username already exist, try another")

    def draw(self):
        # Drawing elements on the board
        self.board_instance.draw_background()
        self.text_drawer.draw_text("REGISTRATION", (255, 255, 255), 100, 180, font)
        self.text_drawer.draw_text("Enter your username: ", (255, 255, 255), 100, 220, font)
        self.username_box.draw_box()
        self.text_drawer.draw_text("Enter your password: ", (255, 255, 255), 100, 320, font)
        self.password_box.draw_box()
        self.submit_btn.process()
        if self.popup_window_invalid.opened:
            self.popup_window_invalid.draw_window(self.board_instance.board)
        if self.popup_window_exist.opened:
            self.popup_window_exist.draw_window(self.board_instance.board)
        pygame.display.update()

    def process_registration(self):
        self.board_instance.image = pygame.transform.scale(self.background_image, (800, 600))
        self.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            self.username_box.handle_event(event)
            self.password_box.handle_event(event)
        if self.submit_btn.alreadyPressed:
            user_credentials = check_username_and_password(self.username_box.get_user_text(),
                                                           self.password_box.get_user_text())
            if user_credentials is None:
                self.popup_window_invalid.draw_window(self.board_instance.board)
                self.popup_window_exist.opened = False
                pygame.display.update()
            else:
                username, password = user_credentials
                if is_user_exist_in_db(DB_NAME, users_table, username):
                    self.popup_window_exist.draw_window(self.board_instance.board)
                    self.popup_window_invalid.opened = False
                    pygame.display.update()
                else:
                    add_valid_user_data_to_db(username, password)

                    # Finish the registration process
                    self.registration = False
                    self.submit_btn.onePress = False
                    self.popup_window_invalid.opened = False if self.popup_window_invalid.opened else self.popup_window_exist.opened
                    # Switch to the main background after registration
                    background_image = pygame.image.load(assets_library['backgrounds']['main_background'])
                    self.board_instance.image = pygame.transform.scale(background_image, (800, 600))
                    pygame.display.update()
                    return username

