import unittest
from unittest.mock import patch, MagicMock
import pygame
from board import Board
from menus.history_menu import HistoryMenu
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.player import Player
from utils import assets_library


class TestEndGameMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.history_menu = HistoryMenu(
			self.test_board)
		self.test_falling = FallingItemsFactory(self.test_board)
		self.test_player = Player(100, 100, self.test_board, self.test_falling, "Test Player")

	def test_history_menu_initialization(self):
		current_image = self.history_menu.background_image
		expected_image = pygame.image.load(assets_library['backgrounds']['registration_page'])

		current_image_str = pygame.image.tostring(current_image, "RGBA")
		expected_image_str = pygame.image.tostring(expected_image, "RGBA")

		self.assertEqual(self.history_menu.board_instance, self.test_board)
		self.assertEqual(self.history_menu.history, True)
		self.assertEqual(current_image_str, expected_image_str)
		self.assertEqual(self.history_menu.column_names, ["Username", "Points", "Life", "Level"])

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('menus.history_menu.Button')
	def test_draw(self, mock_button, mock_scale, mock_load):

		mock_button.return_value.process.return_value = None
		mock_surface = pygame.Surface((800, 600))
		mock_scale.return_value = mock_surface
		mock_font = pygame.font.Font(None, 36)
		mock_font.render.return_value = pygame.Surface((200, 100))

		self.history_menu.draw()

		mock_load.assert_called_once_with(
			assets_library['backgrounds']['registration_page'])
		mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))

		mock_button.assert_called_once_with(
			20, 10, 200, 40, self.history_menu.board_instance, 'BACK TO MENU')
		mock_button_instance = mock_button.return_value
		mock_button_instance.process.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()
