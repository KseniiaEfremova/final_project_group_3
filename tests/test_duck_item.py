import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from board import Board
from models.falling_items.points_falling_item import RubberDuckItem
from utils import assets_library

duck_image = pygame.image.load(assets_library['sprites']['duck'])


class TestDuckItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	@patch('models.falling_items.points_falling_item.RubberDuckItem.spawn')
	def test_duck_item_init(self, mock_spawn):
		duck_item = RubberDuckItem(duck_image, self.test_board)
		mock_spawn.return_value = (0, 0)

		self.assertEqual(duck_item.width, 50)
		self.assertEqual(duck_item.height, 50)
		self.assertEqual(duck_item.speed, 12)
		self.assertEqual(duck_item.points, 10)
		self.assertEqual(duck_item.damage, 0)
		self.assertEqual(duck_item.x, 0)
		self.assertEqual(duck_item.y, 0)

	def test_duck_item_draw(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)
		duck_item.draw(self.test_board)
		duck = pygame.surfarray.array3d(duck_item.image)
		loaded_duck = pygame.transform.scale(duck_image, (50, 59))
		duck_content = pygame.surfarray.array3d(loaded_duck)
		diff = np.abs(duck_content - duck)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_duck_item_spawn(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)

		self.assertTrue(0 < duck_item.x < 800)
		self.assertTrue(-400 < duck_item.y < -100)

	def test_duck_item_fall(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)

		duck_item.y = 400
		duck_item.speed = 5
		duck_item.rect = MagicMock()

		duck_item.disappear = MagicMock()

		duck_item.fall()

		self.assertEqual(duck_item.y, 405)
		self.assertEqual(duck_item.rect.y, 405)
		duck_item.disappear.assert_not_called()

		duck_item.y = 501

		duck_item.fall()

		self.assertEqual(duck_item.y, 506)
		self.assertEqual(duck_item.rect.y, 506)
		duck_item.disappear.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()
