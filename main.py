from board import Board
from player import Player
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
import pygame
import datetime
import time

python_image = pygame.image.load("assets/python.png")
tick_image = pygame.image.load("assets/tick.png")
duck_image = pygame.image.load("assets/duck.png")
bug_image = pygame.image.load("assets/bug.png")
error_image = pygame.image.load("assets/error.gif")
warning_image = pygame.image.load("assets/warning.png")

def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    # player = Player(800 - 725, 600 - 100, 3, 0, 0, game_board, python, tick, duck, warning, error, bug)
    python = PythonItem(python_image, game_board)
    tick = TickItem(tick_image, game_board)
    duck = RubberDuckItem(duck_image, game_board)
    warning = WarningItem(warning_image, game_board)
    error = ErrorItem(error_image, game_board)
    bug = BugItem(bug_image, game_board)
    player = Player(800 - 725, 600 - 100, 3, 0, 0, game_board, python, tick, duck, warning, error, bug)
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
        python.draw(game_board)
        tick.draw(game_board)
        duck.draw(game_board)
        warning.draw(game_board)
        error.draw(game_board)
        bug.draw(game_board)
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
        game_board.draw_timer(remaining_time)
        
        player.draw_player()
        player.move()
        player.check_falling_item_collision()
        game_board.update_display()

if __name__ == '__main__':
    run()
