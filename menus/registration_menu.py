import pygame
from app import check_username_and_password
from board import Board
from button import Button
from input_box import InputBox
from menus.menu import Menu
from text_drawer import TextDrawer
from utils import assets_library

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
