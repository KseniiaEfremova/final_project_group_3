from board import Board
from player import Player
import pygame


def run():
    pygame.init()
    game_board = Board('arcade catcher', (800, 600), 60)
    game_board.display_board()


if __name__ == '__main__':
	run()
