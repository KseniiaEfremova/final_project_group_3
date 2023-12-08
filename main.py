import pygame.display

from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import *
from models.stats.life import Life
from models.stats.level import Level
from models.stats.timer import Timer
from models.stats.points import Points
from menus.pause_menu import PauseMenu
from menus.winning_menu import WinningMenu
from decorators.sounds import Sounds
from utils import assets_library
from menus.registration_menu import RegistrationMenu
from menus.game_over_menu import GameOverMenu
from menus.starting_menu import StartingMenu, show_starting_menu, show_registration_menu


def reset_game(player, falling, winning_menu, is_winner=False):
    player.reset_player_stats()
    player.level = 1
    falling.falling_items.empty()
    winning_menu.play_again = False
    player.points = 0
    if is_winner:
        player.toggle_is_winner()


@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    start_menu = StartingMenu(game_board)
    pause_menu = PauseMenu(game_board)
    winning_menu = WinningMenu(game_board)
    falling = FallingItemsFactory(game_board)
    player = Player(800 - 725, 600 - 200, game_board, falling)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    timer_seconds = 10
    game_over_menu = GameOverMenu(game_board)
    paused_time = 0

    registration_menu = RegistrationMenu(game_board)

    # while registration_menu.registration:
    #     registration_menu.process_registration()

    while start_menu.state == "starting":
        show_starting_menu(start_menu)

        if start_menu.state == "registration":
            show_registration_menu(registration_menu)
            start_menu.state = "starting"

    start_time = time.time()
    
    while True:
        is_winner = player.get_is_winner()
        restart = winning_menu.get_play_again()
        restart_game_over_menu = game_over_menu.get_restart_game()
        game_board.display_board()
        game_board.draw_background()

        if not is_winner:
            life.draw(game_board)
            level.draw(game_board)
            points.draw(game_board)
            player.draw_player()
            falling.create_group()
            falling.draw()

            if life.lives <= 0:
                game_over_menu.draw()
                game_board.update_display()

                if restart_game_over_menu:
                    reset_game(player, falling,winning_menu, is_winner=False)
                    game_board.update_display()
                    start_time = time.time()

            if not game_board.pause:
                if paused_time:
                    start_time += time.time() - paused_time
                    paused_time = 0
                player.move()
                falling.fall_and_respawn()
                player.check_falling_item_collision()
                current_time = time.time()
                elapsed_time = current_time - start_time
                remaining_time = max(timer_seconds - int(elapsed_time), 0)
                timer.draw(game_board, timer=remaining_time)
                game_board.update_display()
                if remaining_time == 0:
                    player.check_is_winner()
                    player.check_for_level_up()
                    if player.leveled_up and player.level < 3:
                        player.level_up_player()
                        level.display_level_up_image(game_board)
                        start_time = time.time()
                        player.reset_player_stats()

            elif game_board.pause:
                if not paused_time:
                    paused_time = time.time()
                    pause_menu.draw()
                    game_board.update_display()

        elif is_winner and restart:
            reset_game(player, falling, winning_menu,is_winner=True)
            game_board.update_display()

        else:
            winning_menu.draw()
            game_board.update_display()

        game_board.update_display()

if __name__ == '__main__':
    run()
