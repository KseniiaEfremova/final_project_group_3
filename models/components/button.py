import pygame
from board import Board
from utils import assets_library

pygame.font.init()
font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 34)


class Button:
    def __init__(
            self, x, y, width, height, board_instance: Board,
            button_text='Button', onclick_function=None, one_press=False):

        """
        Initialise a Button object.

        Parameters:
        - x (int): The x-coordinate of the top-left corner of the button.
        - y (int): The y-coordinate of the top-left corner of the button.
        - width (int): The width of the button.
        - height (int): The height of the button.
        - board_instance (Board): The instance of the game board.
        - buttonText (str): The text to be displayed on the button (default is
        'Button').
        - onclickFunction (callable): The function to be executed when the
        button is clicked.
        - onePress (bool): If True, the onclickFunction is executed only once
        on the first click (default is False).
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_text = button_text
        self.onclick_function = onclick_function
        self.one_press = one_press
        self.board_instance = board_instance

        self.fill_colors = {
            'normal': '#9867c5',
            'hover': '#be93d4',
            'pressed': '#7a4988',
        }
        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.already_pressed = False

    def draw(self):
        button_surf = font.render(
            self.button_text, True, (255, 255, 255))
        self.button_surface.fill(self.fill_colors['normal'])
        self.button_surface.blit(button_surf, [
            self.button_rect.width / 2 - button_surf.get_rect().width / 2,
            self.button_rect.height / 2 - button_surf.get_rect().height / 2
        ])
        self.board_instance.board.blit(self.button_surface, self.button_rect)

    def process(self):

        """
        Process the button's behavior, including handling mouse interactions
        and rendering.
        """

        button_surf = font.render(
            self.button_text, True, (255, 255, 255))

        mouse_pos = pygame.mouse.get_pos()

        self.button_surface.fill(self.fill_colors['normal'])

        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.button_surface.fill(self.fill_colors['pressed'])
                if self.one_press:
                    self.onclick_function()
                elif not self.already_pressed:
                    self.onclick_function()
                    self.already_pressed = True
            else:
                self.already_pressed = False

        self.button_surface.blit(button_surf, [
            self.button_rect.width / 2 - button_surf.get_rect().width / 2,
            self.button_rect.height / 2 - button_surf.get_rect().height / 2
        ])
        self.board_instance.board.blit(self.button_surface, self.button_rect)

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
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'text': self.button_text
        }
