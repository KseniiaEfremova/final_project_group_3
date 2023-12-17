import sys
import pygame
from board import Board
from menus.menu import Menu
from models.components.button import Button
from utils import assets_library


pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 30)


class StartingMenu(Menu):

    """
    Represents the starting menu.

    Attributes:
    - board_instance (Board): The instance of the game board.
    - is_open (bool): Flag indicating whether the starting menu is open.
    - registration (bool): Flag indicating whether the registration menu is active.
    - login (bool): Flag indicating whether the login menu is active.
    - history (bool): Flag indicating whether the history menu is active.
    - instructions (bool): Flag indicating whether the instructions menu is active.
    - credits (bool): Flag indicating whether the credits menu is active.
    - background_image (pygame.Surface): The background image for the starting menu.
    - registration_button (Button): Button for navigating to the registration menu.
    - login_button (Button): Button for navigating to the login menu.
    - history_button (Button): Button for navigating to the history menu.
    - instructions_button (Button): Button for navigating to the instructions menu.
    - credits_button (Button): Button for navigating to the credits menu.
    """
    
    def __init__(self, board_instance: Board):

        """
        Initialise the StartingMenu.

        Parameters:
        - board_instance (Board): The instance of the game board.
        """

        super().__init__(board_instance)
        self.is_open = True
        self.registration = False
        self.login = False
        self.history = False
        self.instructions = False
        self.credits = False
        self.background_pic = assets_library['backgrounds']['registration_page']
        self.registration_button = Button(
            300, 250, 200, 40, self.board_instance,
            'Registration', self.register_handler)
        self.login_button = Button(
            300, 300, 200, 40, self.board_instance,
            'Login', self.login_handler)
        self.history_button = Button(
            300, 350, 200, 40, self.board_instance,
            'History', self.history_handler)
        self.instructions_button = Button(
            300, 400, 200, 40, self.board_instance,
            'Instructions', self.instructions_handler)
        self.credits_button = Button(
            300, 450, 200, 40, self.board_instance,
            'Credits', self.credits_handler)

    def exit_game_handler(self):

        """
        Handles exiting the game.
        """

        pygame.quit()
        sys.exit()

    def register_handler(self):

        """
        Handles the event when the registration button is pressed.
        """

        self.is_open = False
        self.registration = True

    def login_handler(self):

        """
        Handles the event when the login button is pressed.
        """

        self.is_open = False
        self.login = True

    def history_handler(self):

        """
        Handles the event when the history button is pressed.
        """

        self.is_open = False
        self.history = True

    def instructions_handler(self):

        """
        Handles the event when the instructions button is pressed.
        """

        self.is_open = False
        self.instructions = True

    def credits_handler(self):

        """
        Handles the event when the credits button is pressed.
        """

        self.is_open = False
        self.credits = True

    def draw(self):

        """
           Draws the starting menu on the game board.
        """

        background_image = pygame.image.load(self.background_pic)
        background_image = pygame.transform.scale(
            background_image, (800, 600))
        self.board_instance.board.blit(background_image, (0, 0))
        text = font.render("Menu", True, (255, 255, 255))
        self.board_instance.board.blit(text, (350, 180))

        self.registration_button.process()
        self.login_button.process()
        self.history_button.process()
        self.instructions_button.process()
        self.credits_button.process()

    def reset_flags(self):

        """
        Resets all the flags indicating active menus to False.
        """

        self.registration = False
        self.login = False
        self.credits = False
        self.history = False
        self.instructions = False

    def show_registration_menu(self, registration_menu):

        """
        Shows the registration menu.

        Parameters:
        - registration_menu (Menu): The registration menu to show.
        """

        self.is_open = False
        while registration_menu.registration:
            registration_menu.process_registration()

    def show_login_menu(self, login_menu):

        """
        Shows the login menu and returns the username.

        Parameters:
        - login_menu (Menu): The login menu to show.

        Returns:
        - username (str): The username entered in the login menu.
        """

        username = None
        self.is_open = False
        while login_menu.login:
            username = login_menu.process_login()
        return username

    def show_credits_menu(self, credits_menu):

        """
        Shows the credits menu.

        Parameters:
        - credits_menu (Menu): The credits menu to show.
        """

        self.is_open = False
        credits_menu.draw()
        credits_menu.event_handler()

    def show_history_menu(self, history_menu):

        """
        Shows the history menu.

        Parameters:
        - history_menu (Menu): The history menu to show.
        """

        self.is_open = False
        history_menu.draw()
        history_menu.event_handler()

    def show_instructions_menu(self, instructions_menu):

        """
        Shows the instructions menu.

        Parameters:
        - instructions_menu (Menu): The instructions menu to show.
        """

        self.is_open = False
        instructions_menu.draw()
        instructions_menu.event_handler()

    def show_starting_menu(self):

        """
        Displays the starting menu.

        Parameters:
        - start_menu (StartingMenu): The starting menu to display.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game_handler()
        self.draw()




