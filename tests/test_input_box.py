import unittest
import pygame
from unittest.mock import patch, MagicMock
from board import Board
from models.components.input_box import InputBox

pygame.font.init()
pygame.font.Font = MagicMock()
pygame.mouse.get_pos = MagicMock(return_value=(0, 0))


class TestInputBox(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)

    def test_input_initialization(self):
        input = InputBox(0, 0, 100, 50, "Test Input", self.test_board)

        self.assertEqual(input.rect, (0, 0, 100, 50))
        self.assertEqual(input.text, "Test Input")
        self.assertEqual(input.active, False)
        self.assertEqual(input.board_instance, self.test_board)



    def tearDown(self):
        pygame.quit()
        patch.stopall()