from app import check_username_and_password, add_valid_user_data_to_db, DB_NAME, users_table, is_user_exist_in_db
from models.falling_items.falling_items_factory import *
from board import Board
from models.player import Player
from stats.life import Life
from stats.level import Level
from stats.timer import Timer
from stats.points import Points
from menu.pause_menu import PauseMenu
from decorators.sounds import Sounds
from text_drawer import TextDrawer, font
from input_box import InputBox
from button import Button
from utils import assets_library
from pygame.locals import *


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
    start_time = time.time()

    # Initialize registration page elements
    registration = True
    background_image = pygame.image.load(assets_library['backgrounds']['registration_page'])
    username_box = InputBox(250, 250, 140, 32, "", game_board)
    password_box = InputBox(250, 350, 140, 32, "", game_board)
    text_drawer = TextDrawer(game_board)

    submit_btn = Button(300, 420, 200, 40, game_board, 'SUBMIT',
                        lambda: check_username_and_password(username_box.get_user_text(),
                                                            password_box.get_user_text()))

    while True:
        if registration:
            game_board.image = pygame.transform.scale(background_image, (800, 600))
            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    break
                username_box.handle_event(event)
                password_box.handle_event(event)

            # Drawing elements on the screen
            game_board.draw_background()
            text_drawer.draw_text("REGISTRATION", (255, 255, 255), 100, 180, font)
            text_drawer.draw_text("Enter your username: ", (255, 255, 255), 100, 220, font)
            username_box.draw_box()
            text_drawer.draw_text("Enter your password: ", (255, 255, 255), 100, 320, font)
            password_box.draw_box()
            submit_btn.process()
            pygame.display.update()

            # Check if the submit button is pressed
            if submit_btn.alreadyPressed:
                user_credentials = check_username_and_password(username_box.get_user_text(),
                                                               password_box.get_user_text())
                if user_credentials is None:  # if invalid input
                    # TODO: Maybe create a popup window with a warning about invalid username/password
                    submit_btn.onePress = True
                else:
                    username, password = user_credentials
                    if is_user_exist_in_db(DB_NAME, users_table, username):
                        # TODO: Go to the login page
                        pass
                    else:
                        add_valid_user_data_to_db(username, password)
                    registration = False
                    submit_btn.onePress = False

        else:
            # Switch to the main background after registration
            background_image = pygame.image.load(assets_library['backgrounds']['main_background'])
            game_board.image = pygame.transform.scale(background_image, (800, 600))

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
