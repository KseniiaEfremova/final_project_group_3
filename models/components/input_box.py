import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font(None, 40)


class InputBox:

    """
    Represents an input box for text entry in a Pygame application.

    Attributes:
        rect (pygame.Rect): The rectangular area of the input box.
        color_inactive (pygame.Color): The color of the input box when inactive.
        color_active (pygame.Color): The color of the input box when active.
        color (pygame.Color): The current color of the input box.
        text (str): The text entered in the input box.
        txt_surface (pygame.Surface): The rendered text surface.
        active (bool): Flag indicating whether the input box is currently
        active.
        board_instance (Board): The instance of the game board.
        is_password (bool): Flag indicating whether the input box is for a
        password (defaults to False).
    """
    
    def __init__(
            self, x, y, width, height, text, board_instance, is_password=False):

        """
        Initialise an InputBox instance.

        Args:
            x (int): The x-coordinate of the input box.
            y (int): The y-coordinate of the input box.
            width (int): The width of the input box.
            height (int): The height of the input box.
            text (str): The initial text in the input box.
            board_instance (Board): The instance of the game board.
            is_password (bool, optional): Flag indicating whether the input box
            is for a password (defaults to False).
        """

        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('gray15')
        self.color_active = pygame.Color('chartreuse3')
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = pygame.font.Font(
            None, 32).render(text, True,
                             (255, 255, 255))
        self.active = False
        self.board_instance = board_instance
        self.is_password = is_password 

    def handle_event(self, event):

        """
        Handles Pygame events for the input box.

        Args:
            event (pygame.event.Event): The Pygame event to handle.
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else (
                self.color_inactive)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                if self.is_password:
                    self.txt_surface = pygame.font.Font(
                        None, 32).render('*' * len(self.text),
                                         True, (255, 255, 255))
                else:
                    self.txt_surface = pygame.font.Font(
                        None, 32).render(self.text, True,
                                         (255, 255, 255))

    def draw_box(self):

        """
        Draws the input box on the game board.
        """

        width = max(300, self.txt_surface.get_width()+10)
        self.rect.w = width
        self.board_instance.board.blit(
            self.txt_surface, (self.rect.x+5, self.rect.y+4))
        pygame.draw.rect(
            self.board_instance.board, self.color, self.rect, 2)

    def get_user_text(self):

        """
        Gets the text entered in the input box.

        Returns:
            str: The text entered in the input box.
        """

        return self.text

    def get_attributes(self):

        """
        Gets the attributes of an instance.

        Returns:
            dict:
                x: int,
                y: int,
                width: int,
                height: int,
                text: str
        """

        return {
            'x': self.rect.x,
            'y': self.rect.y,
            'width': self.rect.width,
            'height': self.rect.height,
            'text': self.text
        }
