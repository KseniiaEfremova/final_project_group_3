import sys
import pygame
from board import Board
from menus.menu import Menu
from models.components.button import Button
from utils import assets_library

pygame.font.init()
font = pygame.font.Font('assets/fonts/FukuCatch.otf', 120)

class StartingMenu(Menu):
    def __init__(self, board_instance: Board):
        super().__init__(board_instance)
        self.run_display = True
        self.mid_w, self.mid_h = 800 / 2, 600 / 2
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def blit_screen(self):
        self.board_instance.board.blit(self.board.board_surface, (0, 0))
        pygame.display.update()
        self.reset_keys()

class MainMenu(StartingMenu, Menu):
    def __init__(self):
        super().__init__(self)
        self.state = "Start"
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.instructions_x, self.instructions_y =  self.mid_w, self.mid_h + 50
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 70
        self.register_x, self.register_y = self.mid_w, self.mid_h + 90
        self.login_x, self.login_y = self.mid_w, self.mid_h + 110
        self.history_x, self.history_y = self.mid_w, self.mid_h + 130

    def exit_game_handler(self):
        pygame.quit()
        sys.exit()

    def instructions_handler(self):
        pass

    def credits_handler(self):
        pass

    def register_handler(self):
        pass

    def login_handler(self):
        pass

    def draw(self):
        self.run_display = True
        while self.run_display:
            background_image = pygame.image.load(assets_library['backgrounds']['win'])
            image = pygame.transform.scale(background_image, (self.width, self.height))
            text = font.render("Menu", True, (255, 255, 255))
            exit_button = Button(450, 500, 150, 40, self.board_instance,
                                 buttonText='Exit',
                                 onclickFunction=self.exit_game_handler,
                                 onePress=False)
            instructions_button = Button(200, 500, 150, 40, self.board_instance,
                                         buttonText='Instructions',
                                         onclickFunction=self.instructions_handler,
                                         onePress=False)
            credits_button = Button(450, 500, 150, 40, self.board_instance,
                                 buttonText='Credits',
                                 onclickFunction=self.credits_handler,
                                 onePress=False)
            register_button = Button(450, 500, 150, 40, self.board_instance,
                                    buttonText='Register',
                                    onclickFunction=self.register_handler,
                                    onePress=False)
            login_button = Button(450, 500, 150, 40, self.board_instance,
                                    buttonText='Login',
                                    onclickFunction=self.login_handler,
                                    onePress=False)
            self.board_instance.board.blit(image, (0, 0))
            self.board_instance.board.blit(text, (220, 400))
            # buttons.process()


