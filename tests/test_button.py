import unittest
import pygame
from unittest.mock import patch, MagicMock
from board import Board
from models.components.button import Button

pygame.font.init()
pygame.font.Font = MagicMock()
pygame.font.Font.render.return_value = pygame.Surface((200, 100))
pygame.mouse.get_pos = MagicMock(return_value=(0, 0))


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)

    def test_button_initialization(self):
        button = Button(0, 0, 100, 50, self.test_board)

        self.assertEqual(button.x, 0)
        self.assertEqual(button.y, 0)
        self.assertEqual(button.width, 100)
        self.assertEqual(button.height, 50)
        self.assertEqual(button.onclick_function, None)
        self.assertEqual(button.one_press, False)
        self.assertEqual(button.board_instance, self.test_board)
        self.assertFalse(button.already_pressed)

    def test_get_attributes(self):
        button = Button(
            0, 0, 100, 50, self.test_board,
            "This is button")
        actual = button.get_attributes()
        expected = {
            'x': 0,
            'y': 0,
            'width': 100,
            'height': 50,
            'text': "This is button"
        }
        self.assertEqual(actual, expected)

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
