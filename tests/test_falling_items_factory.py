import unittest
from unittest.mock import patch
import pygame
import numpy as np
from board import Board
from models.falling_items.falling_items_factory import FallingItemsFactory
from utils import assets_library


class TestFallingItemsFactory(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.test_falling_items = FallingItemsFactory(self.test_board)

	def test_falling_items_factory_init(self):
		self.assertEqual(self.test_falling_items.timer_seconds, 60)
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.python_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['python']['python1']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.tick_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['tick']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.duck_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['duck']['duck5']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.bug_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['bug']['bug1']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.error_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['error']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.warning_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['warning']), "RGBA"))
		self.assertEqual(self.test_falling_items.game_board, self.test_board)
		self.assertEqual(self.test_falling_items.item_list, [])

	def test_create_group(self):
		self.test_falling_items.create_group()

		self.assertEqual(self.test_falling_items.item_list,
						 [self.test_falling_items.tick,
						  self.test_falling_items.duck,
						  self.test_falling_items.warning,
						  self.test_falling_items.error,
						  self.test_falling_items.bug,
						  self.test_falling_items.python])
		self.assertEqual(len(self.test_falling_items.falling_items), 6)

	# def test_bug_item_draw(self):
	# 	bug_item = BugItem(bug_image, self.test_board)
	# 	bug_item.draw(self.test_board)
	# 	bug = pygame.surfarray.array3d(bug_item.image)
	# 	loaded_bug = pygame.transform.scale(bug_image, (50, 50))
	# 	bug_content = pygame.surfarray.array3d(loaded_bug)
	# 	diff = np.abs(bug_content - bug)
	# 	total_diff = np.sum(diff)
	# 	allowable_diff = 0
	#
	# 	self.assertLessEqual(total_diff, allowable_diff)
	#
	# def test_bug_item_spawn(self):
	# 	bug_item = BugItem(bug_image, self.test_board)
	#
	# 	self.assertFalse(bug_item.x < 0)
	# 	self.assertFalse(bug_item.x == 0)
	# 	self.assertFalse(bug_item.x > 770)
	# 	self.assertTrue(0 < bug_item.x < 770)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
