import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from board import Board
from models.falling_items.damage_falling_item import ErrorItem
from utils import assets_library

error_image = pygame.image.load(assets_library['sprites']['error'])


class TestErrorItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	@patch('models.falling_items.damage_falling_item.ErrorItem.spawn')
	def test_error_item_init(self, mock_spawn):
		error_item = ErrorItem(error_image, self.test_board)
		mock_spawn.return_value = (0, 0)

		self.assertEqual(error_item.width, 50)
		self.assertEqual(error_item.height, 50)
		self.assertEqual(error_item.speed, 5)
		self.assertEqual(error_item.points, 5)
		self.assertEqual(error_item.damage, 10)
		self.assertEqual(error_item.x, 0)
		self.assertEqual(error_item.y, 0)

	def test_error_item_draw(self):
		error_item = ErrorItem(error_image, self.test_board)
		error_item.draw(self.test_board)
		error = pygame.surfarray.array3d(error_item.image)
		loaded_error = pygame.transform.scale(error_image, (50, 50))
		error_content = pygame.surfarray.array3d(loaded_error)
		diff = np.abs(error_content - error)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_error_item_spawn(self):
		error_item = ErrorItem(error_image, self.test_board)

		self.assertTrue(0 < error_item.x < 800)
		self.assertTrue(-400 < error_item.y < -100)

	def test_error_item_fall(self):
		error_item = ErrorItem(error_image, self.test_board)

		error_item.y = 400
		error_item.speed = 5
		error_item.rect = MagicMock()

		error_item.disappear = MagicMock()

		error_item.fall()

		self.assertEqual(error_item.y, 405)
		self.assertEqual(error_item.rect.y, 405)
		error_item.disappear.assert_not_called()

		error_item.y = 501

		error_item.fall()

		self.assertEqual(error_item.y, 506)
		self.assertEqual(error_item.rect.y, 506)
		error_item.disappear.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()


