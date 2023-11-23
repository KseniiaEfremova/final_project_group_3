from board import Board
from player import Player
from falling_items.points_falling_item import PythonItem, TickItem, RubberDuckItem
from falling_items.damage_falling_item import WarningItem, ErrorItem, BugItem
import pygame
import datetime

python_image = pygame.image.load("assets/python.png")
tick_image = pygame.image.load("assets/tick.png")
duck_image = pygame.image.load("assets/duck.png")
bug_image = pygame.image.load("assets/bug.png")
error_image = pygame.image.load("assets/error.gif")
warning_image = pygame.image.load("assets/warning.png")


def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    player = Player(800 - 725, 600 - 100, game_board)
    python = PythonItem(python_image, game_board)
    tick = TickItem(tick_image, game_board)
    duck = RubberDuckItem(duck_image, game_board)
    warning = WarningItem(warning_image, game_board)
    error = ErrorItem(error_image, game_board)
    bug = BugItem(bug_image, game_board)
    long_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=5)
    medium_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=4)
    short_stop = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=3)

    falling_items = []
    level = 0

    while True:
        game_board.display_board()
        game_board.draw_background()
        player.draw_player()
        player.move()

        if len(falling_items) == 0:
            level += 1
            falling_items = [tick, duck, warning, error, bug, python]
            falling_items *= level
        for item in falling_items[:]:
            item.draw(game_board)
            item.fall()
            falling_items.remove(item) # this line makes it glitch 


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


        game_board.update_display()


if __name__ == '__main__':
    run()
