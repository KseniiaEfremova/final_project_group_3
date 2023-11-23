import unittest
import pygame
import numpy as np
from board import Board
from falling_items.points_falling_item import RubberDuckItem

duck_image = pygame.image.load("assets/duck.png")


class TestDuckItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	def test_duck_item_init(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)

		self.assertEqual(duck_item.width, 30)
		self.assertEqual(duck_item.height, 30)
		self.assertEqual(duck_item.y, 0)
		self.assertEqual(duck_item.speed, 8)
		self.assertEqual(duck_item.points, 10)
		self.assertEqual(duck_item.damage, 0)

	def test_duck_item_draw(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)
		duck_item.draw(self.test_board)
		duck = pygame.surfarray.array3d(duck_item.image)
		# change this after adjusting assets
		loaded_duck = pygame.transform.scale(duck_image, (67, 67))
		duck_content = pygame.surfarray.array3d(loaded_duck)
		diff = np.abs(duck_content - duck)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_duck_item_spawn(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)

		self.assertFalse(duck_item.x < 0)
		self.assertFalse(duck_item.x == 0)
		self.assertFalse(duck_item.x > 770)
		self.assertTrue(0 < duck_item.x < 770)

	def test_duck_item_fall(self):
		duck_item = RubberDuckItem(duck_image, self.test_board)
		duck_item.draw(self.test_board)
		duck_item.fall()

		self.assertTrue(duck_item.y > 0)
		self.assertTrue(duck_item.y >= duck_item.speed)