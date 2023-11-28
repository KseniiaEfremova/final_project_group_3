from falling_items.falling_items_factory import *
from board import Board
from player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
from menu.pause_menu import PauseMenu
from utils import assets_library
from decorators.sounds import Sounds
import pygame
import time
falling = FallingItemsFactory()


python_image = pygame.image.load(assets_library['sprites']['python']['python1'])
tick_image = pygame.image.load(assets_library['sprites']['tick'])
duck_image = pygame.image.load(assets_library['sprites']['duck']['duck5'])
bug_image = pygame.image.load(assets_library['sprites']['bug']['bug1'])
error_image = pygame.image.load(assets_library['sprites']['error'])
warning_image = pygame.image.load(assets_library['sprites']['warning'])


@Sounds("assets/sounds/soundtrack.mp3", loop=True)
def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    player = Player(800 - 725, 600 - 200, game_board, falling.python, falling.tick,
                    falling.duck, falling.warning, falling.error, falling.bug)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)

    timer_seconds = 60
    start_time = time.time()

    # timer for making items fall
    falling.create_timer()

    while True:
        game_board.display_board()
        game_board.draw_background()
        # player.draw_player()
        life.draw(game_board)
        level.draw(game_board)
        points.draw(game_board)

            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(timer_seconds - int(elapsed_time), 0)
            timer.draw(game_board, timer=remaining_time)
        elif game_board.pause:
            pause_menu.draw()
            game_board.update_display()
        
        player.draw_player()
        player.move()

        falling.create_group()
        falling.set_fall_timer()
        falling.fall_and_respawn()

        player.check_falling_item_collision()
        game_board.update_display()


if __name__ == '__main__':
    run()
