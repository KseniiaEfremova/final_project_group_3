import unittest
from unittest.mock import patch, MagicMock
import pygame
from board import Board
from models.falling_items.damage_falling_item import DamageFallingItem


class TestPointsFallingItem(unittest.TestCase):
	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.test_board.board = MagicMock(spec=pygame.surface.Surface)

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('pygame.surface.Surface')
	def test_disappear_progress_zero(self, mock_scale, mock_load, mock_surface):
		item = DamageFallingItem("Test", mock_surface, 8,
								 5, 10, 30, 30,
								 0,0, self.test_board)
		item.disappear()
		disappearance_progress = 0
		item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
		item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))

		self.assertEqual(item_width, 120)
		self.assertEqual(item_height, 120)

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('pygame.surface.Surface')
	def test_disappear_progress_two_third_left(self, mock_scale, mock_load,
											   mock_surface):
		item = DamageFallingItem("Test", mock_surface, 8,
								 5, 10, 30, 30,
								 0,0, self.test_board)
		item.disappear()
		disappearance_progress = -1/3
		item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
		item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))

		self.assertEqual(item_width, 150)
		self.assertEqual(item_height, 150)

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('pygame.surface.Surface')
	def test_disappear_progress_one_third_left(self, mock_scale, mock_load,
											   mock_surface):
		item = DamageFallingItem("Test", mock_surface, 8,
								 5, 10, 30, 30,
								 0,0, self.test_board)
		item.disappear()
		disappearance_progress = -2/3
		item_width = max(30, int(30 + 90 * (1 - disappearance_progress)))
		item_height = max(30, int(30 + 90 * (1 - disappearance_progress)))

		self.assertEqual(item_width, 180)
		self.assertEqual(item_height, 180)

	def tearDown(self):
		pygame.quit()
		patch.stopall()


