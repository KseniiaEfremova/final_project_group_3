import pygame
from db.user import check_username_and_password, is_user_exist_in_db, add_valid_user_data_to_db, DB_NAME, users_table
from board import Board
from menus.menu import Menu
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.text_drawer import TextDrawer
from models.components.popup import PopupWindow
from utils import assets_library
from pygame.locals import *

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class RegistrationMenu(Menu):
    def __init__(self, board_instance: Board, registration=True):

        """
        Initialise a RegistrationMenu instance.

        Args:
            board_instance (Board): The instance of the game board.
            registration (bool, optional): Flag indicating whether it's a registration or login menu.
        """

        super().__init__(board_instance)
        self.registration = registration
        self.background_pic = assets_library['backgrounds']['registration_page']
        self.username_box = InputBox(
            250, 250, 140, 32, "",
            self.board_instance)
        self.password_box = InputBox(
            250, 350, 140, 32, "",
            self.board_instance)
        self.text_drawer = TextDrawer(self.board_instance)
        self.submit_btn = Button(
            300, 420, 200, 40, self.board_instance,
            'SUBMIT', lambda: check_username_and_password(
                self.username_box.get_user_text(),
                self.password_box.get_user_text()))
        self.back_btn = Button(
            20, 500, 200, 40, self.board_instance,
            'BACK TO MENU', self.handle_back_to_menu)
        self.popup_window_invalid = PopupWindow(
            800, 40, "Invalid Username or Password!")
        self.popup_window_exist = PopupWindow(
            800, 40,
            "This username already exist, try another")

    def draw(self):

        """
        Draw the registration menu on the board.
        """

        background_img = pygame.image.load(self.background_pic)

        background_image = pygame.transform.scale(
            background_img, (800, 600))

        self.board_instance.board.blit(background_image, (0, 0))
        self.text_drawer.draw_text(
            "REGISTRATION", (255, 255, 255),
            100, 180, font)
        self.text_drawer.draw_text(
            "Enter your username: ", (255, 255, 255),
            100, 220, font)
        self.username_box.draw_box()
        self.text_drawer.draw_text(
            "Enter your password: ", (255, 255, 255),
            100, 320, font)
        self.password_box.draw_box()
        if self.popup_window_invalid.opened:
            self.popup_window_invalid.draw_window(self.board_instance.board)
        if self.popup_window_exist.opened:
            self.popup_window_exist.draw_window(self.board_instance.board)
        self.submit_btn.process()
        self.back_btn.process()
        pygame.display.update()

    def process_registration(self):

        """
        Process the registration input and perform necessary actions.

        Returns:
            str: The username entered by the user during the registration process.
        """

        self.draw()
        pygame.display.update()
        username = self.handle_user_input()
        return username

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            self.username_box.handle_event(event)
            self.password_box.handle_event(event)

        if self.submit_btn.alreadyPressed:
            username = self.process_submit()
            return username

    def process_submit(self):
        user_credentials = check_username_and_password(
            self.username_box.get_user_text(),
            self.password_box.get_user_text()
        )

        if user_credentials is None:
            self.handle_invalid_credentials()
        else:
            username = self.handle_valid_credentials(user_credentials)
            return username

    def handle_invalid_credentials(self):
        self.popup_window_invalid.draw_window(self.board_instance.board)
        self.popup_window_exist.opened = False
        pygame.display.update()

    def handle_valid_credentials(self, user_credentials):
        username, password = user_credentials
        if is_user_exist_in_db(DB_NAME, users_table, username):
            self.popup_window_exist.draw_window(self.board_instance.board)
            self.popup_window_invalid.opened = False
            pygame.display.update()
        else:
            username = self.add_user_to_db(username, password)
            self.finish_registration()
            return username

    def add_user_to_db(self, username, password):
        add_valid_user_data_to_db(username, password)
        return username

    def finish_registration(self):
        self.registration = False
        self.submit_btn.onePress = False
        self.popup_window_invalid.opened = (
            False if self.popup_window_invalid.opened else
            self.popup_window_exist.opened
        )
        self.switch_to_main_background()

    def switch_to_main_background(self):
        background_image = pygame.image.load(
            assets_library['backgrounds']['main_background'])
        self.board_instance.image = pygame.transform.scale(background_image,
                                                           (800, 600))
        pygame.display.update()

    def handle_back_to_menu(self):
        self.registration = False
