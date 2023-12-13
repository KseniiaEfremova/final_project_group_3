import pygame
from menus.menu import Menu
from board import Board
from models.components.button import Button
from utils import assets_library
from menus.starting_menu import show_starting_menu


class CreditsMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.background_image = pygame.image.load(assets_library['backgrounds']['credits'])
        self.back_button = Button(20, 10, 200, 40, self.board_instance, 'BACK TO MENU', self.back_button_handler)
        self.state = "credits"

    def draw(self):
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))
        self.board_instance.board.blit(self.background_image, (0, 0))
        self.back_button.process()
        pygame.display.update()

    #  TODO make the button work
    def back_button_handler(self):
        self.state = "back"


# def back_to_starting_menu(start_menu):
#     start_menu.state = "starting"
#     show_starting_menu()


