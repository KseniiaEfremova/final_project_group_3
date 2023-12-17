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
from menus.starting_menu import StartingMenu
from menus.credits_menu import CreditsMenu
from menus.instructions_menu import InstructionsMenu
from decorators.sounds import Sounds
from utils import assets_library, reset_game





@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run():

    """
    The main function to run the Code Quest game.

    This function initializes the game components, handles user registration
    and login,
    and manages the game loop with different states such as playing, winning,
    and losing.
    """

    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    pause_menu = PauseMenu(game_board)
    winning_menu = EndGameMenu(game_board, assets_library['backgrounds']['win'])
    game_over_menu = EndGameMenu(
        game_board, assets_library['backgrounds']['game_over'])
    falling = FallingItemsFactory(game_board)
    registration_menu = RegistrationMenu(game_board)
    login_menu = LoginMenu(game_board)
    history_menu = HistoryMenu(game_board)
    credits_menu = CreditsMenu(game_board)
    instructions_menu = InstructionsMenu(game_board)
    start_menu = StartingMenu(game_board)

    username = None
    while username is None:
        start_menu.show_starting_menu()

        if start_menu.registration:
            registration_menu.registration = True
            start_menu.show_registration_menu(registration_menu)
            if username is None:
                start_menu.reset_flags()

        if start_menu.login:
            login_menu.login = True
            username = start_menu.show_login_menu(login_menu)
            if username is None:
                start_menu.reset_flags()

        if start_menu.credits:
            credits_menu.credits = True
            while credits_menu.credits:
                start_menu.show_credits_menu(credits_menu)
            start_menu.reset_flags()

        if start_menu.history:
            history_menu.history = True
            while history_menu.history:
                start_menu.show_history_menu(history_menu)
            start_menu.reset_flags()

        if start_menu.instructions:
            instructions_menu.instructions = True
            while instructions_menu.instructions:
                start_menu.show_instructions_menu(instructions_menu)
            start_menu.reset_flags()

        game_board.update_display()

    player = Player(800 - 725, 600 - 200, game_board, falling, "test")
    game_board.display_board(player)
    game_board.draw_background()

    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    timer_seconds = 60
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
            reset_game(
                player, falling, winning_menu, True, False)
            start_time = time.time()
            game_board.update_display()

        elif is_loser and restart_from_loss:
            player.update_db()
            reset_game(
                player, falling, game_over_menu, False, True)
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
