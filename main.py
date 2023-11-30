from models.falling_items.falling_items_factory import *
from board import Board
from models.player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from menu.pause_menu import PauseMenu
from menu.game_over_menu import GameOverMenu
from decorators.sounds import Sounds
from utils import assets_library


@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    pause_menu = PauseMenu(game_board)
<<<<<<< HEAD
    game_over_menu = GameOverMenu(game_board)
    player = Player(800 - 725, 600 - 200, game_board, falling.python, falling.tick, falling.duck, falling.warning, falling.error, falling.bug)
=======
    # winning_menu = WinningMenu(game_board)
    falling = FallingItemsFactory(game_board)
    player = Player(800 - 725, 600 - 200, game_board, falling)
>>>>>>> develop
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
<<<<<<< HEAD

    timer_seconds = 2
    start_time = time.time()

    # timer for making items fall
    falling.create_timer()

    game_over = False

=======
    timer_seconds = 60
    start_time = time.time()
>>>>>>> develop
    while True:
        # winner = True
        winner = False
        game_board.display_board()
        game_board.draw_background()
        life.draw(game_board)
        level.draw(game_board)
        points.draw(game_board)
<<<<<<< HEAD
        if not game_board.pause and not game_over:
=======
        player.draw_player()
        falling.create_group()
        falling.draw()
        if not winner and not game_board.pause:
            player.move()
            falling.fall_and_respawn()
            player.check_falling_item_collision()

            # TODO: stop the timer and save the remaining time when paused
>>>>>>> develop
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(timer_seconds - int(elapsed_time), 0)
            timer.draw(game_board, timer=remaining_time)
<<<<<<< HEAD

            if remaining_time == 0:
                game_over = True

        if game_over:
            game_over_menu.draw()

=======
            game_board.update_display()
>>>>>>> develop
        elif game_board.pause:
            pause_menu.draw()
            game_board.update_display()
        elif winner:
            print('you won')
            # current_time = time.time()
            # elapsed_time = current_time - start_time
            # remaining_time = timer_seconds - int(elapsed_time)
            # winning_menu.draw(counter=remaining_time)
            # game_board.update_display()


if __name__ == '__main__':
    run()
