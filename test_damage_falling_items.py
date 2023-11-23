import unittest
import pygame
from unittest.mock import MagicMock
import datetime
from falling_items.damage_falling_item import DamageFallingItem, WarningItem, ErrorItem, BugItem


class MockBoard:
    def __init__(self):
        self.board = MagicMock(spec=pygame.surface.Surface)


class TestDamageFallingItem(unittest.TestCase):
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
        disappearance_progress = 0
        item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
        item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))
        self.assertEqual(item.y, 500)
        self.assertEqual(item_width, 120)
        self.assertEqual(item_height, 120)

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





class TestBugItem(unittest.TestCase):

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))
        self.mock_board = MockBoard()

    def test_bug_item_init(self):
        bug_item = BugItem(self.mock_surface, self.mock_board)
        self.assertEqual(bug_item.width, 30)
        self.assertEqual(bug_item.height, 30)
        self.assertEqual(bug_item.y, 0)
        self.assertEqual(bug_item.speed, 3)
        self.assertEqual(bug_item.points, 10)
        self.assertEqual(bug_item.damage, 30)


class TestWarningItem(unittest.TestCase):

    def setUp(self):
        self.mock_surface = pygame.Surface((30, 30))
        self.mock_board = MockBoard()

    def test_warning_item(self):
        warning_item = WarningItem(self.mock_surface, self.mock_board)
        self.assertEqual(warning_item.width, 30)
        self.assertEqual(warning_item.height, 30)
        self.assertEqual(warning_item.y, 0)
        self.assertEqual(warning_item.speed, 5)
        self.assertEqual(warning_item.points, 1)
        self.assertEqual(warning_item.damage, 5)