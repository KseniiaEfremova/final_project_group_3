from board import Board
from player import Player
import pygame


def run():
    pygame.init()

    game_board = Board('arcade catcher', (800, 600), 60)
    player = Player(800 - 725, 600 - 100, game_board)
    
    while True:
        game_board.display_board()
        player.move()
        player.draw_player()
        game_board.update_display()

if __name__ == '__main__':
    run()
