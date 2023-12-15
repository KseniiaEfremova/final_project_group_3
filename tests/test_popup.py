import unittest
import pygame
from unittest.mock import patch
from board import Board
from models.components.popup import PopupWindow


class TestPopup(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.popup = PopupWindow(100, 50, "Test Popup")

    def test_popup_initialization(self):

        self.assertEqual(self.popup.rect, pygame.Rect(0, 0, 100, 50))
        self.assertEqual(self.popup.text, "Test Popup")
        self.assertEqual(self.popup.opened, False)

    def test_popup_draw_window(self):
        mock_font = pygame.font.Font(None, 36)
        mock_color = (255, 255, 255)

        self.popup.draw_window(self.test_board.board)

        mock_font.render.assert_called_with("Test Popup", True, mock_color)
        self.assertEqual(self.popup.opened, True)

    def test_get_attributes(self):
        actual = self.popup.get_attributes()
        expected = {
            'x': 0,
            'y': 0,
            'width': 100,
            'height': 50,
            'text': "Test Popup"
        }
        self.assertEqual(actual, expected)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
