import unittest
import pygame
import numpy as np
from board import Board
from falling_items.damage_falling_item import WarningItem

warning_image = pygame.image.load("assets/warning.png")


class TestWarningItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	def test_warning_item_init(self):
		warning_item = WarningItem(warning_image, self.test_board)

		self.assertEqual(warning_item.width, 30)
		self.assertEqual(warning_item.height, 30)
		self.assertEqual(warning_item.y, 0)
		self.assertEqual(warning_item.speed, 5)
		self.assertEqual(warning_item.points, 1)
		self.assertEqual(warning_item.damage, 5)

	def test_warning_item_draw(self):
		warning_item = WarningItem(warning_image, self.test_board)
		warning_item.draw(self.test_board)
		warning = pygame.surfarray.array3d(warning_item.image)
		loaded_warning = pygame.transform.scale(warning_image, (30, 30))
		warning_content = pygame.surfarray.array3d(loaded_warning)
		diff = np.abs(warning_content - warning)
		print(warning_content)
		print(warning)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_warning_item_spawn(self):
		warning_item = WarningItem(warning_image, self.test_board)

		self.assertFalse(warning_item.x < 0)
		self.assertFalse(warning_item.x == 0)
		self.assertFalse(warning_item.x > 770)
		self.assertTrue(0 < warning_item.x < 770)

	def test_warning_item_fall(self):
		warning_item = WarningItem(warning_image, self.test_board)
		warning_item.draw(self.test_board)
		warning_item.fall()

		self.assertTrue(warning_item.y > 0)
		self.assertTrue(warning_item.y >= warning_item.speed)
