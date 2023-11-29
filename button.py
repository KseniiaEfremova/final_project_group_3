import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font(None, 34)

objects = []


class Button:
    def __init__(self, x, y, width, height, board_instance: Board, buttonText='Button', onclickFunction=None, onePress=False):
        """
        Initialize a Button object.

        Parameters:
        - x (int): The x-coordinate of the top-left corner of the button.
        - y (int): The y-coordinate of the top-left corner of the button.
        - width (int): The width of the button.
        - height (int): The height of the button.
        - board_instance (Board): The instance of the game board.
        - buttonText (str): The text to be displayed on the button (default is 'Button').
        - onclickFunction (callable): The function to be executed when the button is clicked.
        - onePress (bool): If True, the onclickFunction is executed only once on the first click (default is False).
        """

        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.board_instance = board_instance

        # Colors for different button states
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        self.alreadyPressed = False
        objects.append(self)

    def process(self):
        """
        Process the button's behavior, including handling mouse interactions and rendering.
        """
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        # Center the text on the button and blit the button surface and text on the game board
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.board_instance.board.blit(self.buttonSurface, self.buttonRect)
