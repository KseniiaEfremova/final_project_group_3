import unittest
from unittest.mock import patch
import pygame
import numpy as np
from board import Board
from models.falling_items.damage_falling_item import WarningItem
from utils import assets_library

warning_image = pygame.image.load(assets_library['sprites']['warning'])


class TestWarningItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	@patch('models.falling_items.damage_falling_item.WarningItem.spawn')
	def test_warning_item_init(self, mock_spawn):
		warning_item = WarningItem(warning_image, self.test_board)
		mock_spawn.return_value = (0, 0)

		self.assertEqual(warning_item.width, 50)
		self.assertEqual(warning_item.height, 50)
		self.assertEqual(warning_item.speed, 12)
		self.assertEqual(warning_item.points, 1)
		self.assertEqual(warning_item.damage, 1)
		self.assertEqual(warning_item.x, 0)
		self.assertEqual(warning_item.y, 0)

	def test_warning_item_draw(self):
		warning_item = WarningItem(warning_image, self.test_board)
		warning_item.draw(self.test_board)
		warning = pygame.surfarray.array3d(warning_item.image)
		loaded_warning = pygame.transform.scale(warning_image, (50, 50))
		warning_content = pygame.surfarray.array3d(loaded_warning)
		diff = np.abs(warning_content - warning)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_warning_item_spawn(self):
		warning_item = WarningItem(warning_image, self.test_board)

		self.assertFalse(warning_item.x < 0)
		self.assertFalse(warning_item.x == 0)
		self.assertFalse(warning_item.x > 770)
		self.assertTrue(0 < warning_item.x < 770)

	def tearDown(self):
		pygame.quit()
		patch.stopall()


