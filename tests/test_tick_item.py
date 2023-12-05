# import unittest
# import pygame
# import numpy as np
# from board import Board
# from models.falling_items.points_falling_item import TickItem
# from utils import assets_library
#
# tick_image = pygame.image.load(assets_library['sprites']['tick'])
#
#
# class TestTickItem(unittest.TestCase):
#
# 	def setUp(self):
# 		pygame.init()
# 		self.board = pygame.display.set_mode(
# 			(800, 600))
# 		self.test_board = Board("Test Board", (800, 600), 60)
#
# 	def test_tick_item_init(self):
# 		tick_item = TickItem(tick_image, self.test_board)
#
# 		self.assertEqual(tick_item.width, 50)
# 		self.assertEqual(tick_item.height, 50)
# 		self.assertEqual(tick_item.y, 0)
# 		self.assertEqual(tick_item.speed, 5)
# 		self.assertEqual(tick_item.points, 1)
# 		self.assertEqual(tick_item.damage, 0)
#
# 	def test_tick_item_draw(self):
# 		tick_item = TickItem(tick_image, self.test_board)
# 		tick_item.draw(self.test_board)
# 		tick = pygame.surfarray.array3d(tick_item.image)
# 		# change this after adjusting assets
# 		loaded_tick = pygame.transform.scale(tick_image, (50, 50))
# 		tick_content = pygame.surfarray.array3d(loaded_tick)
# 		diff = np.abs(tick_content - tick)
# 		total_diff = np.sum(diff)
# 		allowable_diff = 0
#
# 		self.assertLessEqual(total_diff, allowable_diff)
#
# 	def test_tick_item_spawn(self):
# 		tick_item = TickItem(tick_image, self.test_board)
#
# 		self.assertFalse(tick_item.x < 0)
# 		self.assertFalse(tick_item.x == 0)
# 		self.assertFalse(tick_item.x > 770)
# 		self.assertTrue(0 < tick_item.x < 770)
#
# 	def test_tick_item_fall(self):
# 		tick_item = TickItem(tick_image, self.test_board)
# 		tick_item.draw(self.test_board)
# 		tick_item.fall()
#
# 		self.assertTrue(tick_item.y > 0)
# 		self.assertTrue(tick_item.y >= tick_item.speed)