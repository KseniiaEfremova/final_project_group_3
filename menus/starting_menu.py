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
        self.state = "starting"
        self.background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        self.registration_button = Button(300, 250, 200, 40, self.board_instance, 'Registration',
                                          self.register_handler)
        self.login_button = Button(300, 300, 200, 40, self.board_instance, 'Login', self.login_handler)
        self.history_button = Button(300, 350, 200, 40, self.board_instance, 'History', self.history_handler)
        self.instructions_button = Button(300, 400, 200, 40, self.board_instance, 'Instructions',
                                          self.instructions_handler)
        self.credits_button = Button(300, 450, 200, 40, self.board_instance, 'Credits', self.credits_handler)

    def exit_game_handler(self):
        pygame.quit()
        sys.exit()

    def instructions_handler(self):
        self.state = "instructions"

    def credits_handler(self):
        self.state = "credits"

    def register_handler(self):
        self.state = "registration"

    def login_handler(self):
        self.state = "login"

    def history_handler(self):
        self.state = "history"

    def draw(self):
        background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        text = font.render("Menu", True, (255, 255, 255))
        self.board_instance.board.blit(text, (350, 180))

        self.registration_button.process()
        self.login_button.process()
        self.history_button.process()
        self.instructions_button.process()
        self.credits_button.process()
        pygame.display.update()


def show_starting_menu(start_menu):
    while start_menu.state == "starting":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu.exit_game_handler()

        start_menu.draw()
        pygame.display.update()


def show_registration_menu(registration_menu):
    while registration_menu.registration:
        registration_menu.process_registration()


def show_login_menu(login_menu):
    while login_menu.login:
        login_menu.process_login()


def show_history_menu(history_menu):
    history_menu.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def show_credits_menu(credits_menu):
    credits_menu.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def show_instructions_menu(instructions_menu):
    instructions_menu.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
