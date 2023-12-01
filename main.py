from app import check_username_and_password, add_valid_user_data_to_db, DB_NAME, users_table, is_user_exist_in_db
from menus.registration_menu import RegistrationMenu
from models.falling_items.falling_items_factory import *
from board import Board
from models.player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from menus.pause_menu import PauseMenu
from decorators.sounds import Sounds
from utils import assets_library


@Sounds(assets_library['sounds']['soundtrack'], loop=True)
def run():
    pygame.init()
    game_board = Board('Code Quest', (800, 600), 60)
    pause_menu = PauseMenu(game_board)
    # winning_menu = WinningMenu(game_board)
    falling = FallingItemsFactory(game_board)
    player = Player(800 - 725, 600 - 200, game_board, falling)
    life = Life(player, game_board)
    level = Level(player, game_board)
    timer = Timer(player, game_board)
    points = Points(player, game_board)
    timer_seconds = 60

    registration_menu = RegistrationMenu(game_board)

    # Run the registration process while the registration menu is active
    while registration_menu.registration:

        # Set the background image for the registration menu
        game_board.image = pygame.transform.scale(registration_menu.background_image, (800, 600))
        registration_menu.draw()
        for event in pygame.event.get():
            registration_menu.username_box.handle_event(event)
            registration_menu.password_box.handle_event(event)

        # Check if the submit button is pressed
        if registration_menu.submit_btn.alreadyPressed:
            user_credentials = check_username_and_password(registration_menu.username_box.get_user_text(),
                                                           registration_menu.password_box.get_user_text())
            if user_credentials is None:  # if invalid input
                # TODO: Create a popup window with a warning about invalid username/password
                registration_menu.submit_btn.onePress = True
            else:
                username, password = user_credentials
                if is_user_exist_in_db(DB_NAME, users_table, username):
                    # TODO: Go to the login page
                    pass
                else:
                    add_valid_user_data_to_db(username, password)

                # Finish the registration process
                registration_menu.registration = False
                registration_menu.submit_btn.onePress = False

                # Switch to the main background after registration
                background_image = pygame.image.load(assets_library['backgrounds']['main_background'])
                game_board.image = pygame.transform.scale(background_image, (800, 600))

    start_time = time.time()
    while True:
        winner = False
        game_board.display_board()
        game_board.draw_background()
        life.draw(game_board)
        level.draw(game_board)
        points.draw(game_board)
        player.draw_player()
        falling.create_group()
        falling.draw()
        if not winner and not game_board.pause:
            player.move()
            falling.fall_and_respawn()
            player.check_falling_item_collision()

            # TODO: stop the timer and save the remaining time when paused
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = max(timer_seconds - int(elapsed_time), 0)
            timer.draw(game_board, timer=remaining_time)
            game_board.update_display()
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
