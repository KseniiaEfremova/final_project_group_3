from models.falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
from models.falling_items.points_falling_item import TickItem, PythonItem, RubberDuckItem
from utils import assets_library
from board import Board
import pygame
import datetime
import time


class FallingItemsFactory(pygame.sprite.Sprite):
    """
    Factory class for creating and managing falling items in Code Quest.

    Attributes:
        timer_seconds (int): The duration of the falling items phase in seconds.
        start_time (float): The start time of the falling items phase.
        python_image (pygame.Surface): The image for Python falling items.
        tick_image (pygame.Surface): The image for Tick falling items.
        duck_image (pygame.Surface): The image for Rubber Duck falling items.
        bug_image (pygame.Surface): The image for Bug falling items.
        error_image (pygame.Surface): The image for Error falling items.
        warning_image (pygame.Surface): The image for Warning falling items.
        falling_items (pygame.sprite.Group): A group containing all falling items.
        game_board (Board): An instance of the game board.
        python (PythonItem): An instance of PythonItem for creating Python falling items.
        tick (TickItem): An instance of TickItem for creating Tick falling items.
        duck (RubberDuckItem): An instance of RubberDuckItem for creating Rubber Duck falling items.
        warning (WarningItem): An instance of WarningItem for creating Warning falling items.
        error (ErrorItem): An instance of ErrorItem for creating Error falling items.
        bug (BugItem): An instance of BugItem for creating Bug falling items.
        item_list (list): A list containing all types of falling items.
    """
    
    def __init__(self, board_instance: Board):
        """
        Initialise a FallingItemsFactory object.

        Parameters:
            board_instance (Board): An instance of the game board.
        """
        super().__init__()
        self.timer_seconds = 60
        self.start_time = time.time()
        self.python_image = pygame.image.load(assets_library['sprites']['python']['python1'])
        self.tick_image = pygame.image.load(assets_library['sprites']['tick'])
        self.duck_image = pygame.image.load(assets_library['sprites']['duck']['duck5'])
        self.bug_image = pygame.image.load(assets_library['sprites']['bug']['bug1'])
        self.error_image = pygame.image.load(assets_library['sprites']['error'])
        self.warning_image = pygame.image.load(assets_library['sprites']['warning'])
        self.falling_items = pygame.sprite.Group()
        self.game_board = board_instance
        self.python = PythonItem(self.python_image, self.game_board)
        self.tick = TickItem(self.tick_image, self.game_board)
        self.duck = RubberDuckItem(self.duck_image, self.game_board)
        self.warning = WarningItem(self.warning_image, self.game_board)
        self.error = ErrorItem(self.error_image, self.game_board)
        self.bug = BugItem(self.bug_image, self.game_board)
        self.item_list = []

    def create_group(self):
        """
        Create a group of falling items for the current game phase.
        """
        self.item_list = [self.tick, self.duck, self.warning, self.error, self.bug, self.python]
        for item in self.item_list:
            self.falling_items.add(item)

    def draw(self):
        """
        Draw all falling items on the game board.
        """
        for sprite in self.falling_items.sprites():
            sprite.draw(self.game_board)

    def fall_and_respawn(self):
        """
        Move all falling items down the screen and handle respawning.
        """
        for sprite in self.falling_items.sprites():
            if isinstance(sprite, TickItem) or isinstance(sprite, WarningItem):
                sprite.fall()
            if isinstance(sprite, PythonItem) or isinstance(sprite, ErrorItem):
                sprite.fall()
            if isinstance(sprite, RubberDuckItem) or isinstance(sprite, BugItem):
                sprite.fall()
