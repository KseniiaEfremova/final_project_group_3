import unittest
from unittest.mock import patch
import pygame
import numpy as np
from board import Board
from models.falling_items.points_falling_item import PythonItem
from utils import assets_library

python_image = pygame.image.load(assets_library['sprites']['python']['python1'])


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
		self.assertEqual(python_item.speed, 8)
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

		self.assertFalse(python_item.x < 0)
		self.assertFalse(python_item.x == 0)
		self.assertFalse(python_item.x > 770)
		self.assertTrue(0 < python_item.x < 770)

	def tearDown(self):
		pygame.quit()
		patch.stopall()