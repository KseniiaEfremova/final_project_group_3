import sys
import pygame
from menus.menu import Menu
from board import Board
from models.components.button import Button
from utils import assets_library


class InstructionsMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.background_pic = assets_library['backgrounds']['instructions']
        self.back_button = Button(0, 560, 190, 40, self.board_instance,
                             'BACK TO MENU', self.back_button_handler)
        self.instructions = True

    def draw(self):
        background_img = pygame.image.load(self.background_pic)
        background_image = pygame.transform.scale(background_img, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        self.back_button.process()
        pygame.display.update()

    def back_button_handler(self):
        self.instructions = False
