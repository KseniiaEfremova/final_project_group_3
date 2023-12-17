import pygame

pygame.font.init()
font = pygame.font.Font(None, 24)


class PopupWindow:

    """
    Represents a popup window in Code Quest.

    Attributes:
        width (int): The width of the popup window.
        height (int): The height of the popup window.
        text (str): The text to be displayed in the popup window.
        x (int): The x-coordinate of the top-left corner of the popup window
        (default is 0).
        y (int): The y-coordinate of the top-left corner of the popup window
        (default is 0).
        opened (bool): Flag indicating whether the popup window is open
        (default is False).
        rect (pygame.Rect): Rectangle defining the position and size of the
        popup window.
    """
    
    def __init__(self, width, height, text, x=0, y=0, opened=False):
        """
        Initialise a PopupWindow object.

        Parameters:
            width (int): The width of the popup window.
            height (int): The height of the popup window.
            text (str): The text to be displayed in the popup window.
            x (int): The x-coordinate of the top-left corner of the popup window
            (default is 0).
            y (int): The y-coordinate of the top-left corner of the popup window
            (default is 0).
            opened (bool): Flag indicating whether the popup window is open
            (default is False).
        """

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.opened = opened

    def draw_window(self, board):

        """
        Draw the popup window on the specified game board.

        Parameters:
            board (pygame.Surface): The game board surface.
        """

        color = pygame.Color('brown2')
        pygame.draw.rect(board, color, self.rect)
        text_surface = font.render(
            self.text, True, (255, 255, 255))

        location = text_surface.get_rect()
        start_text = int(self.rect.width / 2 - location.center[0])

        board.blit(
            text_surface, (self.rect.x + start_text, self.rect.y + 12))

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

