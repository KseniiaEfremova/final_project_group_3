import pygame
from db.user import (check_username_and_password, is_user_exist_in_db,
                     DB_NAME, users_table, check_passwords, get_password_by_username)
from board import Board
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.popup import PopupWindow
from models.components.text_drawer import TextDrawer
from menus.menu import Menu
from utils import assets_library
from pygame.locals import *

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class LoginMenu(Menu):
    """
    Represents the login menu for user sign-up.

    Attributes:
        login (bool): Flag indicating whether it's a login or sign-up menu.
        background_image (pygame.Surface): The background image for the login
        menu.
        username_box (InputBox): Input box for entering the username.
        password_box (InputBox): Input box for entering the password.
        text_drawer (TextDrawer): Drawer for displaying text on the board.
        submit_btn (Button): Button for submitting the login or sign-up.
        back_btn (Button): Button for returning to the main menu.
        popup_window_incorrect (PopupWindow): Popup window for displaying
        incorrect credentials message.
    """

    def __init__(self, board_instance: Board, login=True):
        super().__init__(board_instance)
        self.login = login
        self.background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        self.username_box = InputBox(
            250, 250, 140, 32, "", self.board_instance)
        self.password_box = InputBox(
            250, 350, 140, 32, "", self.board_instance)
        self.text_drawer = TextDrawer(self.board_instance)
        self.submit_btn = Button(
            300, 450, 200, 40, self.board_instance, 'SUBMIT',
            lambda: check_username_and_password(
                self.username_box.get_user_text(),
                self.password_box.get_user_text()))
        self.back_btn = Button(
            0, 560, 190, 40, self.board_instance, 'BACK TO MENU',
            self.handle_back_to_menu)
        self.popup_window_incorrect = PopupWindow(
            800, 40, "Incorrect Username or Password!")

    def draw(self):

        """
        Draw the login menu on the board.

        Display elements like background, title, input boxes, buttons,
        and popup window.
        """

        self.board_instance.draw_background()
        self.text_drawer.draw_text(
            "LOGIN", (255, 255, 255), 100, 180, font)
        self.text_drawer.draw_text(
            "Username: ", (255, 255, 255), 100, 220,
            font)
        self.username_box.draw_box()
        self.text_drawer.draw_text(
            "Password: ", (255, 255, 255), 100, 320,
            font)
        self.password_box.draw_box()
        self.submit_btn.process()
        self.back_btn.process()
        if self.popup_window_incorrect.opened:
            self.popup_window_incorrect.draw_window(self.board_instance.board)
        pygame.display.update()

    def handle_user_input(self):
        """
        Handle user input events.

        Capture and handle events like quitting, input box handling, and button presses.
        """

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            self.username_box.handle_event(event)
            self.password_box.handle_event(event)
            if self.submit_btn.alreadyPressed:
                return self.process_submit()
            elif event.type == self.back_btn.alreadyPressed:
                self.handle_back_to_menu()

    def process_submit(self):
        """
        Process the submission of login or sign-up credentials.

        Check if the username and password are correct, and take appropriate actions.

        Returns:
            str: username.
        """
        username, password = (self.username_box.get_user_text(),
                              self.password_box.get_user_text())
        if (is_user_exist_in_db(DB_NAME, users_table, username)
                and check_passwords(password, get_password_by_username(
                    DB_NAME, users_table, username))):
            self.handle_correct_credentials()
        else:
            self.handle_incorrect_credentials()
        return username

    def handle_incorrect_credentials(self):

        """
        Handle incorrect login or sign-up credentials.

        Open the popup window indicating incorrect credentials.
        """

        self.popup_window_incorrect.opened = True

    def handle_correct_credentials(self):

        """
        Handle correct login or sign-up credentials.

        Close the popup window and finish the login process.
        """

        self.popup_window_incorrect.opened = False
        self.finish_login()

    def finish_login(self):

        """
        Finish the login process and switch to the main background.

        Set flags, reset button states, and switch to the main background.
        """

        self.login = False
        self.submit_btn.onePress = False
        self.popup_window_incorrect.opened = False
        self.switch_to_main_background()

    def switch_to_main_background(self):

        """
        Switch to the main background.

        Load the main background image and update the display.
        """

        background_image = pygame.image.load(
            assets_library['backgrounds']['main_background'])
        self.board_instance.image = pygame.transform.scale(background_image,
                                                           (800, 600))
        pygame.display.update()

    def handle_back_to_menu(self):
        """
        Handle going back to the main menu.
        """
        self.login = False

    def process_login(self):

        """
        Process the login menu.

        Set up the background, draw elements, and handle user input.

        Returns:
            str: The username entered by the user during the login process.
        """

        self.board_instance.image = pygame.transform.scale(
            self.background_image, (800, 600))
        self.draw()
        return self.handle_user_input()
