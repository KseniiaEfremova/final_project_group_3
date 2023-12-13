import unittest
from unittest.mock import patch
import pygame
from board import Board
from menus.pause_menu import PauseMenu


class TestPauseMenu(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.pause_menu = PauseMenu(self.test_board)

    def test_pause_menu_initialization(self):
        self.assertEqual(self.pause_menu.board_instance, self.test_board)

    def test_draw(self):
        mock_font = pygame.font.Font(None, 36)
        mock_color = (255, 255, 255)

        self.pause_menu.draw()

        mock_font.render.assert_called_with("Game paused", True, mock_color)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
