import unittest
import pygame
import numpy as np
from board import Board
from models.falling_items.damage_falling_item import BugItem

bug_image = pygame.image.load("assets/bug.png")


class TestBugItem(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode(
			(800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)

	def test_bug_item_init(self):
		bug_item = BugItem(bug_image, self.test_board)

		self.assertEqual(bug_item.width, 30)
		self.assertEqual(bug_item.height, 30)
		self.assertEqual(bug_item.y, 0)
		self.assertEqual(bug_item.speed, 3)
		self.assertEqual(bug_item.points, 10)
		self.assertEqual(bug_item.damage, 30)

	def test_bug_item_draw(self):
		bug_item = BugItem(bug_image, self.test_board)
		bug_item.draw(self.test_board)
		bug = pygame.surfarray.array3d(bug_item.image)
		loaded_bug = pygame.transform.scale(bug_image, (30, 30))
		bug_content = pygame.surfarray.array3d(loaded_bug)
		diff = np.abs(bug_content - bug)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	def test_bug_item_spawn(self):
		bug_item = BugItem(bug_image, self.test_board)

		self.assertFalse(bug_item.x < 0)
		self.assertFalse(bug_item.x == 0)
		self.assertFalse(bug_item.x > 770)
		self.assertTrue(0 < bug_item.x < 770)

	def test_bug_item_fall(self):
		bug_item = BugItem(bug_image, self.test_board)
		bug_item.draw(self.test_board)
		bug_item.fall()

		self.assertTrue(bug_item.y > 0)
		self.assertTrue(bug_item.y >= bug_item.speed)