import pygame
from board import Board

pygame.font.init()
font = pygame.font.Font(None, 40)


class InputBox:
    def __init__(self, x, y, width, height, text, board_instance: Board):
        """
       Initialize an InputBox object.

       Parameters:
       - x (int): The x-coordinate of the top-left corner of the input box.
       - y (int): The y-coordinate of the top-left corner of the input box.
       - width (int): The width of the input box.
       - height (int): The height of the input box.
       - text (str): The initial text in the input box.
       - board_instance (Board): The instance of the game board.
       """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.active = False
        self.color = pygame.Color('gray15')
        self.board_instance = board_instance

    # Handle mouse and keyboard events for the input box.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # deleting last char
            elif event.key == pygame.K_RETURN:
                pass
            else:
                self.text += event.unicode

    def draw_box(self):
        self.color = pygame.Color('gray15') if not self.active else pygame.Color("chartreuse3")
        pygame.draw.rect(self.board_instance.board, self.color, self.rect, 2)

        text_surface = font.render(self.text, True, (255, 255, 255))

        self.board_instance.board.blit(text_surface, (self.rect.x + 5, self.rect.y + 4))
        self.rect.w = max(300, text_surface.get_width() + 10)

    def get_user_text(self):
        """
        Get the text entered the input box.

        Returns:
        - str: The text entered the input box.
        """
        return self.text

    def get_attributes(self):
        return {
            'x': self.rect.x,
            'y': self.rect.y,
            'width': self.rect.width,
            'height': self.rect.height,
            'text': self.text
        }
