import pygame
from user import check_username_and_password, is_user_exist_in_db, add_valid_user_data_to_db, DB_NAME, users_table
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
    """ Represents the registration menu for user sign-up. """
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

    def draw(self):
        # Drawing elements on the board
        self.board_instance.draw_background()
        self.text_drawer.draw_text("REGISTRATION", (255, 255, 255), 100, 180, font)
        self.text_drawer.draw_text("Enter your username: ", (255, 255, 255), 100, 220, font)
        self.username_box.draw_box()
        self.text_drawer.draw_text("Enter your password: ", (255, 255, 255), 100, 320, font)
        self.password_box.draw_box()
        self.submit_btn.process()
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
                # TODO: Create a popup window with a warning about invalid username/password
                print("invalid username/password")
                pass
            else:
                username, password = user_credentials
                if is_user_exist_in_db(DB_NAME, users_table, username):
                    # TODO: Create a popup window that this username already exist, chose an another username
                    print("this username already exist, chose an another username")
                    pass
                else:
                    add_valid_user_data_to_db(username, password)

                    # Finish the registration process
                    self.registration = False
                    self.submit_btn.onePress = False

                    # Switch to the main background after registration
                    background_image = pygame.image.load(assets_library['backgrounds']['main_background'])
                    self.board_instance.image = pygame.transform.scale(background_image, (800, 600))

