import unittest
from unittest.mock import MagicMock, patch
import pygame
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.stats.points import Points
from utils import assets_library


class TestPoints(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.test_falling_items = FallingItemsFactory(self.test_board)
        self.test_player = Player(100, 100, self.test_board, self.test_falling_items)
        self.points = Points(self.test_player, self.test_board)

    def test_level_initialization(self):
        self.assertEqual(self.points.board_instance, self.test_board)
        self.assertEqual(self.points.x, 500)
        self.assertEqual(self.points.y, 75)
        self.assertEqual(self.points.points, self.test_player.points)

    def test_update(self):
        self.test_player.points = 0
        self.points.update()
        self.assertEqual(self.points.points, 0)

        self.test_player.points = 999
        self.points.update()
        self.assertEqual(self.points.points, 999)

        self.test_player.points = -564
        self.points.update()
        self.assertEqual(self.points.points, -564)

    def test_draw(self):
        mock_font = pygame.font.Font(None,36)
        mock_color = (255, 255, 255)
        self.points.points = 100
        self.points.draw(self.test_board)

        mock_font.render.assert_called_with(f"Points: {self.points.points}", True, mock_color)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
