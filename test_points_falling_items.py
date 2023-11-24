import unittest
import pygame
from unittest.mock import MagicMock
import datetime
from falling_items.damage_falling_item import DamageFallingItem, WarningItem, ErrorItem, BugItem


class MockBoard:
    def __init__(self):
        self.board = MagicMock(spec=pygame.surface.Surface)


class TestPointsFallingItem(unittest.TestCase):
    pygame.image.load = MagicMock()
    pygame.transform.scale = MagicMock()

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))
        self.mock_board = MockBoard()

    def test_disappear_progress_zero(self):
        item = DamageFallingItem("Test", self.mock_surface, 8, 5, 10, 30, 30, 0,
                                 0, self.mock_board)
        stop_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
        item.disappear(stop_time)
        self.assertEqual(item.y, 500)

    def test_disappear_progress_two_third_left(self):
        item = DamageFallingItem("Test", self.mock_surface, 8, 5, 10, 30, 30, 0,
                                 0, self.mock_board)
        stop_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
        item.disappear(stop_time)
        disappearance_progress = -1/3
        item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
        item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))
        self.assertEqual(item.y, 500)
        self.assertEqual(item_width, 150)
        self.assertEqual(item_height, 150)

    def test_disappear_progress_one_third_left(self):
        item = DamageFallingItem("Test", self.mock_surface, 8, 5, 10, 30, 30, 0,
                                 0, self.mock_board)
        stop_time = datetime.datetime(2023, 1, 1, 0, 0, 0)
        item.disappear(stop_time)
        disappearance_progress = -2/3
        item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
        item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))
        self.assertEqual(item.y, 500)
        self.assertEqual(item_width, 180)
        self.assertEqual(item_height, 180)

    def test_disappear_progress_done(self):
        # TODO: provide tests to check if item disappear if progress is done
        pass


