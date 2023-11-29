from models.falling_items.falling_items_factory import *
from board import Board
from models.player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from menu.pause_menu import PauseMenu
from decorators.sounds import Sounds
from utils import assets_library

player_level = 1
@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run(player_level):
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    pause_menu = PauseMenu(game_board)
    # winning_menu = WinningMenu(game_board)
    falling = FallingItemsFactory(game_board)
    player = Player(800 - 725, 600 - 200, player_level, game_board, falling)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    timer_seconds = 60
    start_time = time.time()
    while True:
        # winner = True
        winner = False
        game_board.display_board()
        game_board.draw_background()
        life.draw(game_board)
        level.draw(game_board)
        points.update()
        points.draw(game_board)
        player.draw_player()
        falling.create_group()
        falling.draw()
        if not winner and not player.loser and not game_board.pause:
            player.move()
            falling.fall_and_respawn()
            player.check_falling_item_collision()

            # TODO: stop the timer and save the remaining time when paused
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(timer_seconds - int(elapsed_time), 0)
            timer.draw(game_board, timer=remaining_time)
            game_board.update_display()
            if remaining_time == 0:
                player.check_for_level_up()
                if player.leveled_up:
                    player_level += 1
                    level.display_level_up_image(game_board)
                    run(player_level)
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
        elif player.loser:
            print("You lost!")
            break


if __name__ == '__main__':
    run(player_level)
