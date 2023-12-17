import unittest
from unittest.mock import MagicMock
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
				assets_library['sprites']['python']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.tick_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['tick']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.duck_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['duck']), "RGBA"))
		self.assertEqual(pygame.image.tostring(
			self.test_falling_items.bug_image, "RGBA"),
			pygame.image.tostring(pygame.image.load(
				assets_library['sprites']['bug']), "RGBA"))
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

	def test_draw(self):
		mock_sprite_1 = MagicMock(spec=pygame.sprite.Sprite)
		mock_sprite_2 = MagicMock(spec=pygame.sprite.Sprite)
		mock_sprite_1.draw = MagicMock()
		mock_sprite_2.draw = MagicMock()

		self.test_falling_items.item_list = [mock_sprite_1, mock_sprite_2]
		for item in self.test_falling_items.item_list:
			self.test_falling_items.falling_items.add(item)

		self.test_falling_items.draw()

		mock_sprite_1.draw.assert_called_with(self.test_board)
		mock_sprite_2.draw.assert_called_with(self.test_board)

	def test_fall_and_respawn(self):
		mock_sprite_1 = MagicMock(spec=pygame.sprite.Sprite)
		mock_sprite_2 = MagicMock(spec=pygame.sprite.Sprite)
		mock_sprite_1.fall = MagicMock()
		mock_sprite_2.fall = MagicMock()

		self.test_falling_items.item_list = [mock_sprite_1, mock_sprite_2]
		for item in self.test_falling_items.item_list:
			self.test_falling_items.falling_items.add(item)

		self.test_falling_items.fall_and_respawn()

		mock_sprite_1.fall.assert_called()
		mock_sprite_2.fall.assert_called()

	def tearDown(self):
		pygame.quit()
