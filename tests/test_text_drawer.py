import unittest
import pygame
from unittest.mock import patch, MagicMock
from board import Board
from models.components.text_drawer import TextDrawer
from utils import assets_library


class TestTextDrawer(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.text = TextDrawer(self.test_board)

    def test_text_initialization(self):

        self.assertEqual(self.text.board_instance, self.test_board)

    def test_draw_text(self):
        mock_font = pygame.font.Font(None,36)
        mock_color = (255, 255, 255)

        self.text.draw_text("Code Quest", mock_color, 100, 200, mock_font)

        mock_font.render.assert_called_with("Code Quest", True, mock_color)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()