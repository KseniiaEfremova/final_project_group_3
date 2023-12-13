import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from board import Board
from models.falling_items.damage_falling_item import BugItem
from utils import assets_library

bug_image = pygame.image.load(assets_library['sprites']['bug']['bug1'])


class TestBugItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	@patch('models.falling_items.damage_falling_item.BugItem.spawn')
	def test_bug_item_init(self, mock_spawn):
		bug_item = BugItem(bug_image, self.test_board)
		mock_spawn.return_value = (0, 0)

		self.assertEqual(bug_item.width, 50)
		self.assertEqual(bug_item.height, 50)
		self.assertEqual(bug_item.speed, 8)
		self.assertEqual(bug_item.points, 10)
		self.assertEqual(bug_item.damage, 30)
		self.assertEqual(bug_item.x, 0)
		self.assertEqual(bug_item.y, 0)

	def test_bug_item_draw(self):
		bug_item = BugItem(bug_image, self.test_board)
		bug_item.draw(self.test_board)
		bug = pygame.surfarray.array3d(bug_item.image)
		loaded_bug = pygame.transform.scale(bug_image, (50, 50))
		bug_content = pygame.surfarray.array3d(loaded_bug)
		diff = np.abs(bug_content - bug)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_bug_item_spawn(self):
		bug_item = BugItem(bug_image, self.test_board)

		self.assertTrue(bug_item.width < bug_item.x < 800 - bug_item.width)
		self.assertTrue(-400 < bug_item.y < -100)

	def test_bug_item_fall(self):
		bug_item = BugItem(bug_image, self.test_board)

		bug_item.y = 400
		bug_item.speed = 5
		bug_item.rect = MagicMock()

		bug_item.disappear = MagicMock()

		bug_item.fall()

		self.assertEqual(bug_item.y, 405)
		self.assertEqual(bug_item.rect.y, 405)
		bug_item.disappear.assert_not_called()

		bug_item.y = 501

		bug_item.fall()

		self.assertEqual(bug_item.y, 506)
		self.assertEqual(bug_item.rect.y, 506)
		bug_item.disappear.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()
