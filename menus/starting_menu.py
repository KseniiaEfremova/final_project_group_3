import sys
import pygame
from board import Board
from menus.menu import Menu
from models.components.button import Button
from utils import assets_library


pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)


class StartingMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.is_open = True
        self.registration = False
        self.login = False
        self.history = False
        self.instructions = False
        self.credits = False
        self.background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        self.registration_button = Button(
            300, 250, 200, 40, self.board_instance,
            'Registration', self.register_handler)
        self.login_button = Button(
            300, 300, 200, 40, self.board_instance,
            'Login', self.login_handler)
        self.history_button = Button(
            300, 350, 200, 40, self.board_instance,
            'History', self.history_handler)
        self.instructions_button = Button(
            300, 400, 200, 40, self.board_instance,
            'Instructions', self.instructions_handler)
        self.credits_button = Button(
            300, 450, 200, 40, self.board_instance,
            'Credits', self.credits_handler)

    def exit_game_handler(self):
        pygame.quit()
        sys.exit()

    def register_handler(self):
        self.is_open = False
        self.registration = True

    def login_handler(self):
        self.is_open = False
        self.login = True

    def history_handler(self):
        self.is_open = False
        self.history = True

    def instructions_handler(self):
        self.is_open = False
        self.instructions = True

    def credits_handler(self):
        self.is_open = False
        self.credits = True

    def draw(self):
        background_image = pygame.image.load(
            assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(
            background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        text = font.render("Menu", True, (255, 255, 255))
        self.board_instance.board.blit(text, (350, 180))

        self.registration_button.process()
        self.login_button.process()
        self.history_button.process()
        self.instructions_button.process()
        self.credits_button.process()
        pygame.display.update()

    def reset_flags(self):
        self.registration = False
        self.login = False
        self.credits = False
        self.history = False
        self.instructions = False

    def show_registration_menu(self, registration_menu):
        self.is_open = False
        while registration_menu.registration:
            registration_menu.process_registration()

    def show_login_menu(self, login_menu):
        username = None
        self.is_open = False
        while login_menu.login:
            username = login_menu.process_login()
        return username

    def show_credits_menu(self, credits_menu):
        self.is_open = False
        credits_menu.draw()
        credits_menu.event_handler()
        pygame.display.update()

    def show_history_menu(self, history_menu):
        self.is_open = False
        history_menu.draw()
        history_menu.event_handler()
        pygame.display.update()

    def show_instructions_menu(self, instructions_menu):
        self.is_open = False
        instructions_menu.draw()
        instructions_menu.event_handler()
        pygame.display.update()


def show_starting_menu(start_menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_menu.exit_game_handler()

    start_menu.draw()
    pygame.display.update()



