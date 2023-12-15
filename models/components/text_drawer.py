import pygame
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)


class TextDrawer:

    """
    Handles drawing text on the game board in Code Quest.

    Attributes:
        board_instance (Board): An instance of the game board where text is to be drawn.
    """

    def __init__(self, board_instance: Board):

        """
        Initialise a TextDrawer object.

        Parameters:
            board_instance (Board): An instance of the game board where text is to be drawn.
        """

        self.board_instance = board_instance

    def draw_text(self, text, text_color, x, y, font):

        """
        Draw text on the game board, calculating centre position for the text.

        Parameters:
            text (str): The text to be drawn.
            text_color (tuple): The color of the text in RGB format.
            x (int): The x-coordinate for the starting position of the text.
            y (int): The y-coordinate for the starting position of the text.
            font (pygame.font.Font): The font used for the text.
        """

        img = font.render(text, True, text_color)
        location = img.get_rect()

        start_text = int(self.board_instance.res[0] / 2 - location.center[0])
        self.board_instance.board.blit(img, (start_text, y))
