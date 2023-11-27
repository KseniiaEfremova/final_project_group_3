from board import Board
from player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
from menu.pause_menu import PauseMenu
from menu.winning_menu import WinningMenu
from utils import assets_library
from decorators.sounds import Sounds
import pygame
import datetime
import time


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
    python = PythonItem(python_image, game_board)
    tick = TickItem(tick_image, game_board)
    duck = RubberDuckItem(duck_image, game_board)
    warning = WarningItem(warning_image, game_board)
    error = ErrorItem(error_image, game_board)
    bug = BugItem(bug_image, game_board)
    pause_menu = PauseMenu(game_board)
    winning_menu = WinningMenu(game_board)
    player = Player(800 - 725, 600 - 200, game_board, python, tick, duck, warning, error, bug)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    long_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=5)
    medium_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=4)
    short_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=3)
    timer_seconds = 60
    start_time = time.time()

    while True:
        game_board.display_board()
        game_board.draw_background()
        life.draw(game_board)
        level.draw(game_board)
        points.draw(game_board)
        python.draw(game_board)
        tick.draw(game_board)
        duck.draw(game_board)
        warning.draw(game_board)
        error.draw(game_board)
        bug.draw(game_board)
        winner = True
        if not game_board.pause and not winner:
            python.fall()
            tick.fall()
            duck.fall()
            warning.fall()
            error.fall()
            bug.fall()
            if python.y >= 500:
                python.disappear(medium_stop)
            if tick.y >= 500:
                tick.disappear(short_stop)
            if duck.y >= 500:
                duck.disappear(long_stop)
            if warning.y >= 500:
                warning.disappear(short_stop)
            if error.y >= 500:
                error.disappear(medium_stop)
            if bug.y >= 500:
                bug.disappear(long_stop)

            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(timer_seconds - int(elapsed_time), 0)
            timer.draw(game_board, timer=remaining_time)
        elif game_board.pause:
            pause_menu.draw()
            game_board.update_display()
        elif winner:
            winning_menu.draw()
            game_board.update_display()
        
        player.draw_player()
        player.move()
        player.check_falling_item_collision()
        game_board.update_display()


if __name__ == '__main__':
    run()
