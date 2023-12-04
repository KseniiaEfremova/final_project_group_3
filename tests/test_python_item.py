import unittest
import pygame
import numpy as np
from board import Board
from falling_items.points_falling_item import PythonItem

python_image = pygame.image.load("assets/python.png")


class TestPythonItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	def test_python_item_init(self):
		python_item = PythonItem(python_image, self.test_board)

		self.assertEqual(python_item.width, 30)
		self.assertEqual(python_item.height, 30)
		self.assertEqual(python_item.y, 0)
		self.assertEqual(python_item.speed, 12)
		self.assertEqual(python_item.points, 5)
		self.assertEqual(python_item.damage, 0)

	def test_python_item_draw(self):
		python_item = PythonItem(python_image, self.test_board)
		python_item.draw(self.test_board)
		python = pygame.surfarray.array3d(python_item.image)
		# change this after adjusting assets
		loaded_python = pygame.transform.scale(python_image, (100, 100))
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

	def test_python_item_fall(self):
		python_item = PythonItem(python_image, self.test_board)
		python_item.draw(self.test_board)
		python_item.fall()

		self.assertTrue(python_item.y > 0)
		self.assertTrue(python_item.y >= python_item.speed)