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
        self.assertEqual(button.onclickFunction, None)
        self.assertEqual(button.onePress, False)
        self.assertEqual(button.board_instance, self.test_board)
        self.assertFalse(button.alreadyPressed)

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

    # def test_process_button_behavior(self):
    #     mock_onclick_function = MagicMock()
    #     button = Button(
    #         0, 0, 100, 50, self.test_board,
    #         onclickFunction=mock_onclick_function)
    #     f = pygame.font.Font(None, 40)
    #     f.render.return_value = pygame.surface.Surface((200, 200))
    #     button.process()
        # pygame.mouse.get_pos = MagicMock(return_value=(25, 25))
        #

        # button.process()
        # self.assertEqual(button.buttonSurface.fill.call_args[0][0], button.fillColors['hover'])
        # pygame.mouse.get_pressed = MagicMock(return_value=(True, False, False))
        # button.process()
        # self.assertEqual(button.buttonSurface.fill.call_args[0][0], button.fillColors['pressed'])
        # mock_onclick_function.assert_called_once()

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()
