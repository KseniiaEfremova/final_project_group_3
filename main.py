from board import Board
from player import Player
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
import pygame
import datetime


def run():
    pygame.init()

    game_board = Board('Code Quest', (800, 600), 60)
    player = Player(800 - 725, 600 - 100, game_board)
    python = PythonItem(game_board)
    tick = TickItem(game_board)
    duck = RubberDuckItem(game_board)
    warning = WarningItem(game_board)
    error = ErrorItem(game_board)
    bug = BugItem(game_board)
    tick_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=4)
    python_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=2)
    duck_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=.5)
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
            python.disappear(python_stop)
        if tick.y >= 500:
            tick.disappear(tick_stop)
        if duck.y >= 500:
            duck.disappear(duck_stop)
        if warning.y >= 500:
            warning.disappear(python_stop)
        if error.y >= 500:
            error.disappear(tick_stop)
        if bug.y >= 500:
            bug.disappear(duck_stop)
        player.draw_player()
        player.move()
        game_board.update_display()


if __name__ == '__main__':
    run()
