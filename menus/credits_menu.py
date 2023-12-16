import pygame
from menus.menu import Menu
from board import Board
from models.components.button import Button
from utils import assets_library


class CreditsMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.background_pic = assets_library['backgrounds']['credits']
        self.credits = True
        self.back_btn = Button(20, 550, 200, 40, self.board_instance, 'BACK TO MENU',
                               self.back_button_handler)

    def draw(self):
        background_image = pygame.image.load(assets_library['backgrounds']['credits'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        self.back_btn.process()
        pygame.display.update()

    def back_button_handler(self):
        self.credits = False
