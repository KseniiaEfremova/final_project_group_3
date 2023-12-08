import unittest
import pygame
import numpy as np
from unittest.mock import patch, MagicMock
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from utils import assets_library


class TestBoard(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def test_board_initialization(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        self.assertEqual(test_board.name, name)
        self.assertEqual(test_board.res, res)
        self.assertEqual(test_board.frames, frames)

    def test_display_board_initialization(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_falling = FallingItemsFactory(test_board)
        test_player = Player(100, 100, test_board, test_falling, "Test Player")
        test_board.display_board(test_player)

        self.assertEqual(pygame.display.get_caption()[0], "TestBoard")

    def test_update_display_board(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_result = test_board.update_display()

        self.assertEqual(test_result, 'Display updated')

    def test_draw_background(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)
        test_board.draw_background()
        board_content = pygame.surfarray.array3d(test_board.board)
        loaded_background = pygame.image.load(assets_library['backgrounds']['main_background'])
        loaded_background = pygame.transform.scale(loaded_background, res)
        background_content = pygame.surfarray.array3d(loaded_background)
        diff = np.abs(board_content - background_content)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertEqual(board_content.shape, background_content.shape)
        self.assertLessEqual(total_diff, allowable_diff)

    @patch('models.player.Player')
    def test_quit_event_handling(self, mock_player):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        mock_player_instance = mock_player.return_value
        mock_player_instance.points = 100  # Set points attribute
        mock_player_instance.life = 3      # Set life attribute
        mock_player_instance.level = 1     # Set level attribute
        mock_player_instance.user_id = 123

        with patch('pygame.event.get', return_value=[MagicMock(type=pygame.QUIT)]):
            with self.assertRaises(SystemExit):
                test_board.display_board(mock_player_instance)

    def tearDown(self):
        pygame.quit()
        patch.stopall()
