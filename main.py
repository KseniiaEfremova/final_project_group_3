import sys
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import *
from models.stats.life import Life
from models.stats.level import Level
from models.stats.timer import Timer
from models.stats.points import Points
from menus.registration_menu import RegistrationMenu
from menus.login_menu import LoginMenu
from menus.history_menu import HistoryMenu
from menus.pause_menu import PauseMenu
from menus.end_game_menu import EndGameMenu
from decorators.sounds import Sounds
from utils import assets_library


def reset_game(player, falling, end_game_menu, is_winner, is_loser):
    """
    Resets the game state.

    Args:
        player (Player): The player object.
        falling (FallingItemsFactory): The falling items factory object.
        end_game_menu (EndGameMenu): The end game menu object.
        is_winner (bool): True if the player won, False otherwise.
        is_loser (bool): True if the player lost, False otherwise.
    """
    player.reset_player()
    player.reset_player_stats()
    falling.falling_items.empty()
    end_game_menu.play_again = False
    if is_winner:
        player.toggle_is_winner()
    if is_loser:
        player.toggle_is_loser()


def show_history_menu(history_menu):
    """
    Displays the history menu.

    Args:
        history_menu (HistoryMenu): The history menu object.
    """
    history_menu.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run():
    """
    The main function to run the Code Quest game.

    This function initializes the game components, handles user registration and login,
    and manages the game loop with different states such as playing, winning, and losing.
    """
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    pause_menu = PauseMenu(game_board)
    winning_menu = EndGameMenu(game_board, assets_library['backgrounds']['win'])
    game_over_menu = EndGameMenu(game_board, assets_library['backgrounds']['game_over'])
    falling = FallingItemsFactory(game_board)
    registration_menu = RegistrationMenu(game_board)
    login_menu = LoginMenu(game_board)
    history_menu = HistoryMenu(game_board)

    while registration_menu.registration:
        username = registration_menu.process_registration()

    while login_menu.login:
        username = login_menu.process_login()
        
    # while history_menu.history:
    #     show_history_menu(history_menu)

    player = Player(800 - 725, 600 - 200, game_board, falling, 'test')
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    timer_seconds = 30
    paused_time = 0
    start_time = time.time()
    
    while True:
        is_winner = player.get_is_winner()
        is_loser = player.get_is_loser()
        restart_from_win = winning_menu.get_play_again()
        restart_from_loss = game_over_menu.get_play_again()
        game_board.display_board(player)
        game_board.draw_background()

        if not is_winner and not is_loser:
            life.draw(game_board)
            level.draw(game_board)
            points.draw(game_board)
            player.draw_player()
            falling.create_group()
            falling.draw()

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
                        player.reset_player()

            elif game_board.pause:
                pause_menu.draw()
                if not paused_time:
                    paused_time = time.time()
                    game_board.update_display()

        elif is_winner and restart_from_win:
            player.update_db()
            reset_game(player, falling, winning_menu, True, False)
            start_time = time.time()
            game_board.update_display()

        elif is_loser and restart_from_loss:
            player.update_db()
            reset_game(player, falling, game_over_menu, False, True)
            start_time = time.time()
            game_board.update_display()

        elif is_winner:
            player.update_db()
            winning_menu.draw()
            game_board.update_display()

        elif is_loser:
            player.update_db()
            game_over_menu.draw()
            game_board.update_display()

        game_board.update_display()


if __name__ == '__main__':
    run()
