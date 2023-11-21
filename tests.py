import unittest
import pygame
import sys
from unittest.mock import patch, MagicMock
from board import Board  # Assuming your class is in a file named "board.py"


class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        self.assertEqual(test_board.name, name)
        self.assertEqual(test_board.res, res)
        self.assertEqual(test_board.frames, frames)

    def test_quit_event_handling(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        with patch('pygame.event.get', return_value=[MagicMock(type=pygame.QUIT)]):
            with self.assertRaises(SystemExit):
                test_board.display_board()

    @patch('pygame.init')
    @patch('pygame.display.set_caption')
    @patch('pygame.display.set_mode')
    @patch('pygame.time.Clock')
    def test_display_board_initialization(self, mock_clock, mock_set_mode, mock_set_caption, mock_init):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        test_board.display_board()

        mock_init.assert_called_once()
        mock_set_caption.assert_called_once_with(name)
        mock_set_mode.assert_called_once_with(res)
        mock_clock_instance = mock_clock.return_value
        mock_clock_instance.tick.assert_called_once_with(frames)





