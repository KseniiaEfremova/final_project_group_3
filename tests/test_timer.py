import unittest
from unittest.mock import patch
import pygame
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.stats.timer import Timer


class TestPoints(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.test_falling_items = FallingItemsFactory(self.test_board)
        self.test_player = Player(100, 100, self.test_board, self.test_falling_items)
        self.timer = Timer(self.test_player, self.test_board)

    def test_timer_initialization(self):
        self.assertEqual(self.timer.board_instance, self.test_board)
        self.assertEqual(self.timer.x, 10)
        self.assertEqual(self.timer.y, 75)

    def test_draw(self):
        mock_font = pygame.font.Font(None,36)
        mock_color = (255, 255, 255)
        timer = 23
        self.timer.draw(self.test_board, timer=timer)

        mock_font.render.assert_called_with(f"Time: {timer}", True, mock_color)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
