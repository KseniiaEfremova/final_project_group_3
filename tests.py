import unittest
import pygame
import numpy as np
from unittest.mock import patch, MagicMock
import datetime
from board import Board
from player import Player
from falling_items.damage_falling_item import DamageFallingItem, WarningItem, ErrorItem, BugItem



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
        test_board.display_board()

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
        loaded_background = pygame.image.load("assets/background.jpg")
        loaded_background = pygame.transform.scale(loaded_background, res)
        background_content = pygame.surfarray.array3d(loaded_background)
        diff = np.abs(board_content - background_content)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertEqual(board_content.shape, background_content.shape)
        self.assertLessEqual(total_diff, allowable_diff)

    def test_quit_event_handling(self):
        name = "TestBoard"
        res = (800, 600)
        frames = 60
        test_board = Board(name, res, frames)

        with patch('pygame.event.get', return_value=[MagicMock(type=pygame.QUIT)]):
            with self.assertRaises(SystemExit):
                test_board.display_board()

    def tearDown(self):
        pygame.quit()


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode(
            (800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)

    def test_player_initialization(self):
        player = Player(100, 100, self.test_board)

        self.assertEqual(player.rect.center, (100, 100))
        self.assertEqual(player.width, 100)
        self.assertEqual(player.height, 90)

    def test_draw_player(self):
        player = Player(100, 100, self.test_board)
        player.draw_player()
        player = pygame.surfarray.array3d(player.image)
        loaded_player = pygame.image.load("assets/player.png")
        loaded_player = pygame.transform.scale(loaded_player, (100,100))
        player_content = pygame.surfarray.array3d(loaded_player)
        diff = np.abs(player_content - player)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertLessEqual(total_diff, allowable_diff)

    @patch('player.pygame.key.get_pressed')
    def test_player_movement(self, mock_get_pressed):
        self.player = Player(100, 100, self.test_board)
        initial_x = self.player.rect.x
        # check why this move is only to the right
        self.player.move()
        self.assertEqual(self.player.rect.x, initial_x + 10)

    @patch('player.pygame.key.get_pressed')
    def test_boundary_checking(self, mock_get_pressed):
        self.player = Player(100, 100, self.test_board)
        self.player.rect.x = 0
        # check why this move is only to the right
        self.player.move()
        self.assertEqual(self.player.rect.x, 10)

        self.player.rect.x = self.test_board.res[0] - self.player.width
        self.player.move()
        expected_x = self.test_board.res[0] - self.player.width
        self.assertEqual(self.player.rect.x, expected_x)

    def tearDown(self):
        pygame.quit()

pygame.image.load = MagicMock()
pygame.transform.scale = MagicMock()
class MockBoard:
    def __init__(self):
        self.board = MagicMock(spec=pygame.surface.Surface)


class TestDamageFallingItem(unittest.TestCase):
    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))  # Create a mock surface
        self.mock_board = MockBoard()

    def test_disappear(self):
        item = DamageFallingItem("Test", self.mock_surface, 8, 5, 10, 30, 30, 0,
                                 0, self.mock_board)
        stop_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
        item.disappear(stop_time)

        # Add assertions for the expected behavior during disappearance
        # For example, check if the image is scaled and blitted correctly


class TestErrorItem(unittest.TestCase):

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))  # Create a mock surface
        self.mock_board = MockBoard()

    def test_error_item(self):
        error_item = ErrorItem(self.mock_surface, self.mock_board)

        # Add assertions for the expected behavior of ErrorItem
        # For example, check if it initializes correctly and inherits from DamageFallingItem


class TestBugItem(unittest.TestCase):

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))  # Create a mock surface
        self.mock_board = MockBoard()

    def test_bug_item(self):
        bug_item = BugItem(self.mock_surface, self.mock_board)

        # Add assertions for the expected behavior of BugItem
        # For example, check if it initializes correctly and inherits from DamageFallingItem


class TestWarningItem(unittest.TestCase):

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))  # Create a mock surface
        self.mock_board = MockBoard()

    def test_warning_item(self):
        warning_item = WarningItem(self.mock_surface, self.mock_board)
