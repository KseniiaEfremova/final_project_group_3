import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from board import Board
from models.falling_items.points_falling_item import PythonItem
from utils import assets_library

python_image = pygame.image.load(assets_library['sprites']['python'])


class TestPythonItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	@patch('models.falling_items.points_falling_item.PythonItem.spawn')
	def test_python_item_init(self, mock_spawn):
		python_item = PythonItem(python_image, self.test_board)
		mock_spawn.return_value = (0, 0)

		self.assertEqual(python_item.width, 50)
		self.assertEqual(python_item.height, 50)
		self.assertEqual(python_item.speed, 6)
		self.assertEqual(python_item.points, 5)
		self.assertEqual(python_item.damage, 0)
		self.assertEqual(python_item.x, 0)
		self.assertEqual(python_item.y, 0)

	def test_python_item_draw(self):
		python_item = PythonItem(python_image, self.test_board)
		python_item.draw(self.test_board)
		python = pygame.surfarray.array3d(python_item.image)
		loaded_python = pygame.transform.scale(python_image, (50, 88))
		python_content = pygame.surfarray.array3d(loaded_python)
		diff = np.abs(python_content - python)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_python_item_spawn(self):
		python_item = PythonItem(python_image, self.test_board)

		self.assertTrue(0 < python_item.x < 800)
		self.assertTrue(-400 < python_item.y < -100)

	def test_python_item_fall(self):
		python_item = PythonItem(python_image, self.test_board)

		python_item.y = 400
		python_item.speed = 5
		python_item.rect = MagicMock()

		python_item.disappear = MagicMock()

		python_item.fall()

		self.assertEqual(python_item.y, 405)
		self.assertEqual(python_item.rect.y, 405)
		python_item.disappear.assert_not_called()

		python_item.y = 501

		python_item.fall()

		self.assertEqual(python_item.y, 506)
		self.assertEqual(python_item.rect.y, 506)
		python_item.disappear.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()
