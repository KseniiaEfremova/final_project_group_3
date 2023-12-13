import pygame
from db.user import *
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
    """ Represents the login menu for user sign-up. """
    def __init__(self, board_instance: Board, login=True):
        super().__init__(board_instance)
        self.login = login
        self.background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        self.username_box = InputBox(
            250, 250, 140, 32, "",
            self.board_instance)
        self.password_box = InputBox(
            250, 350, 140, 32, "",
            self.board_instance)
        self.text_drawer = TextDrawer(self.board_instance)
        self.submit_btn = Button(
            300, 450, 200, 40, self.board_instance,
            'SUBMIT', lambda: check_username_and_password(
                self.username_box.get_user_text(),
                self.password_box.get_user_text()))
        self.back_btn = Button(
            20, 500, 200, 40, self.board_instance,
            'BACK TO MENU', lambda: check_username_and_password(
                self.username_box.get_user_text(),
                self.password_box.get_user_text()))
        self.popup_window_incorrect = PopupWindow(
            800, 40, "Incorrect Username or Password!")

    def draw(self):
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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            self.username_box.handle_event(event)
            self.password_box.handle_event(event)

        if self.submit_btn.alreadyPressed:
            return self.process_submit()
        if self.back_btn.alreadyPressed:
            self.handle_back_to_menu()

    def process_submit(self):
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
        self.popup_window_incorrect.opened = True

    def handle_correct_credentials(self):
        self.popup_window_incorrect.opened = False
        self.finish_login()

    def finish_login(self):
        self.login = False
        self.submit_btn.onePress = False
        self.popup_window_incorrect.opened = False
        self.switch_to_main_background()

    def switch_to_main_background(self):
        background_image = pygame.image.load(
            assets_library['backgrounds']['main_background'])
        self.board_instance.image = pygame.transform.scale(background_image,
                                                           (800, 600))
        pygame.display.update()

    def handle_back_to_menu(self):
        #  TODO go to start menu
        print("go to START MENU")
        pass

    def process_login(self):
        self.board_instance.image = pygame.transform.scale(
            self.background_image, (800, 600))
        self.draw()
        return self.handle_user_input()
