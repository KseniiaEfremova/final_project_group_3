import sys
import pygame
from menus.menu import Menu
from board import Board
from models.components.button import Button
from utils import assets_library


class CreditsMenu(Menu):
    """
    Represents the credits menu.

    Attributes:
    - board_instance (Board): The instance of the game board.
    - background_image (pygame.Surface): The background image for the credits menu.
    - credits (bool): Flag indicating whether the credits menu is active.
    - back_btn (Button): Button for going back to the main menu.
    
    """

    def __init__(self, board_instance: Board):
        """
        Initialise the CreditsMenu.

        Parameters:
        - board_instance (Board): The instance of the game board.
        """
        super().__init__(board_instance)
        self.background_image = pygame.image.load(assets_library['backgrounds']['credits'])
        self.credits = True
        self.back_btn = Button(0, 560, 190, 40, self.board_instance, 'BACK TO MENU',
                               self.back_button_handler)

    def draw(self):
        """
        Draws the credits menu on the game board.
        """
        background_image = pygame.image.load(assets_library['backgrounds']['credits'])
        background_image = pygame.transform.scale(background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        self.back_btn.process()
        pygame.display.update()

    def event_handler(self):
        """
        Handles events for the credits menu, such as quitting the game or going back to the main menu.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.back_button_handler()

    def back_button_handler(self):
        """
        Handles the event when the back button is pressed, setting the credits flag to False.
        """
        self.credits = False
