from board import Board
from player import Player
import pygame


def run():
    pygame.init()
    timer_seconds = 60
    start_time = time.time()

    game_board = Board('arcade catcher', (800, 600), 60)
    player = Player(800 - 725, 600 - 100, game_board)
    
    while True:
        game_board.display_board()
        game_board.draw_background()
        player.draw_player()
        player.move()
        game_board.update_display()

        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(timer_seconds - int(elapsed_time), 0)
        game_board.draw_timer(remaining_time)

if __name__ == '__main__':
    run()
