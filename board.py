import pygame
import sys
from utils import assets_library


background_image = pygame.image.load(
    assets_library['backgrounds']['main_background'])


class Board:
    """
    Represents the game board in Code Quest.

    Attributes:
        name (str): The name of the game.
        res (tuple): The resolution of the game board as a tuple (width, height).
        frames (int): The number of frames per second for display.
        image (pygame.Surface): The background image of the game board.
        board (pygame.Surface): The main surface of the game board.
        board_surface (pygame.Surface): An additional surface for rendering.
        pause (bool): Flag indicating whether the game is paused.
        over (bool): Flag indicating whether the game is over.
    """
    def __init__(self, name, res, frames):
        """
        Initialise the Board object.

        Parameters:
            name (str): The name of the game.
            res (tuple): The resolution of the game board as a tuple (width, height).
            frames (int): The number of frames per second for display.
        """
        self.name = name
        self.res = res
        self.frames = frames
        self.image = pygame.transform.scale(background_image, self.res)
        self.board = pygame.display.set_mode(self.res)
        self.board_surface = pygame.surface.Surface(
            (self.res[0], self.res[1]), pygame.SRCALPHA)
        self.pause = False
        self.over = False
        self.credits = False
    
    def display_board(self, player):
        """
        Handles quit and pause events and updates the display caption with the name.
        Updates the database on forced quit.

        Args:
            player (Player): The player object.
        """
        pygame.display.set_caption(self.name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.update_db()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause

    def update_display(self):
        """
        Updates the display and controls the frames per second.

        Returns:
            str: A message indicating that the display has been updated.
        """
        fps = pygame.time.Clock()
        pygame.display.update()
        fps.tick(self.frames)
        return 'Display updated'

    def draw_background(self):
        """
        Draws the background on the game board.
        """
        self.board.fill('black')
        self.board.blit(self.board_surface, (0, 0))
        self.board.blit(self.image, (0, 0))
