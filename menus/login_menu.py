import pygame
from db.user import check_username_and_password, is_user_exist_in_db, DB_NAME, users_table, \
    check_passwords, get_password_by_username
from board import Board
from models.components.button import Button
from models.components.input_box import InputBox
from menus.menu import Menu
from models.components.text_drawer import TextDrawer
from utils import assets_library
from pygame.locals import *

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class LoginMenu(Menu):
    """ Represents the login menu for user sign-up. """
    def __init__(self, board_instance: Board, login=True):
        super().__init__(board_instance)
        self.login = login
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.username_box = InputBox(250, 250, 140, 32, "", self.board_instance)
        self.password_box = InputBox(250, 350, 140, 32, "", self.board_instance)
        self.text_drawer = TextDrawer(self.board_instance)
        self.submit_btn = Button(300, 420, 200, 40, self.board_instance, 'SUBMIT',
                                 lambda: check_username_and_password(self.username_box.get_user_text(),
                                                                     self.password_box.get_user_text()))
        self.back_btn = Button(20, 10, 200, 40, self.board_instance, 'BACK TO MENU',
                                 lambda: check_username_and_password(self.username_box.get_user_text(),
                                                                     self.password_box.get_user_text()))

    def draw(self):
        # Drawing elements on the board
        self.board_instance.draw_background()
        self.text_drawer.draw_text("LOGIN", (255, 255, 255), 100, 180, font)
        self.text_drawer.draw_text("Username: ", (255, 255, 255), 100, 220, font)
        self.username_box.draw_box()
        self.text_drawer.draw_text("Password: ", (255, 255, 255), 100, 320, font)
        self.password_box.draw_box()
        self.submit_btn.process()
        self.back_btn.process()
        pygame.display.update()

    def process_login(self):
        self.board_instance.image = pygame.transform.scale(self.background_image, (800, 600))
        self.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            self.username_box.handle_event(event)
            self.password_box.handle_event(event)
        if self.submit_btn.alreadyPressed:
            username, password = self.username_box.get_user_text(), self.password_box.get_user_text()
            if (is_user_exist_in_db(DB_NAME, users_table, username)
                    and check_passwords(password, get_password_by_username(DB_NAME, users_table, username))):
                self.login = False
                self.submit_btn.onePress = False

                # Switch to the main background after login
                background_image = pygame.image.load(assets_library['backgrounds']['main_background'])
                self.board_instance.image = pygame.transform.scale(background_image, (800, 600))
                return username

            else:
                #  TODO popup window with a message "Incorrect username or password"
                print("Incorrect username or password")
        if self.back_btn.alreadyPressed:
            #  TODO go to start menu
            print("go to START MENU")
            pass



