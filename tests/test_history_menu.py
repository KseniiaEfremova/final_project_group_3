import unittest
from unittest.mock import patch, MagicMock, call
import pygame
from board import Board
from menus.history_menu import HistoryMenu
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.player import Player
from utils import assets_library


class TestHistoryMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.history_menu = HistoryMenu(
			self.test_board)
		self.test_falling = FallingItemsFactory(self.test_board)
		self.test_player = Player(100, 100, self.test_board,
									self.test_falling, "Test Player")

	def test_history_menu_initialization(self):
		current_image = self.history_menu.background_image
		expected_image = pygame.image.load(
			assets_library['backgrounds']['registration_page'])

		current_image_str = pygame.image.tostring(
			current_image, "RGBA")
		expected_image_str = pygame.image.tostring(
			expected_image, "RGBA")

		self.assertEqual(self.history_menu.board_instance, self.test_board)
		self.assertEqual(self.history_menu.history, True)
		self.assertEqual(current_image_str, expected_image_str)
		self.assertEqual(self.history_menu.column_names,
						 ["Username", "Points", "Life", "Level"])

	def test_draw_columns(self):
		mock_surface = MagicMock()
		mock_font = pygame.font.Font(None, 36)
		mock_color = (255, 255, 255)

		self.history_menu.draw_columns(mock_surface)

		expected_calls = [
			call(mock_font.render(
				'Username', True, mock_color), (150, 230)),
			call(mock_font.render(
				'Points', True, mock_color), (300, 230)),
			call(mock_font.render(
				'Life', True, mock_color), (450, 230)),
			call(mock_font.render(
				'Level', True, mock_color), (600, 230)),
		]

		mock_surface.blit.assert_has_calls(expected_calls)

	@patch('menus.history_menu.get_history_data')
	def test_draw_rows(self, mock_get_history_data):
		test_data = [
			('Test123', -2, 0, 3), ('test', 9, 89, 1),
			('szam', 0, 90, 1), ('gorilla', 0, -12, 1),
			('doggy', 0, -1, 1), ('paskudzio', 0, -1, 1),
			('alba', 0, -3, 1), ('pablo', 0, 90, 1)
		]
		mock_get_history_data.return_value = test_data
		mock_surface = MagicMock()
		mock_font = pygame.font.Font(None, 36)
		mock_color = (255, 255, 255)

		self.history_menu.draw_rows(mock_surface)

		expected_calls = [
			call(mock_font.render(
				'Test123', True, mock_color), (150, 270)),
			call(mock_font.render(
				'-2', True, mock_color), (300, 270)),
			call(mock_font.render(
				'0', True, mock_color), (450, 270)),
			call(mock_font.render(
				'3', True, mock_color), (600, 270)),
			call(mock_font.render(
				'test', True, mock_color), (150, 300)),
			call(mock_font.render(
				'9', True, mock_color), (300, 300)),
			call(mock_font.render(
				'89', True, mock_color), (450, 300)),
			call(mock_font.render(
				'1', True, mock_color), (600, 300)),
			call(mock_font.render(
				'szam', True, mock_color), (150, 330)),
			call(mock_font.render(
				'0', True, mock_color), (300, 330)),
			call(mock_font.render(
				'90', True, mock_color), (450, 330)),
			call(mock_font.render(
				'1', True, mock_color), (600, 330)),
			call(mock_font.render(
				'gorilla', True, mock_color), (150, 360)),
			call(mock_font.render(
				'0', True, mock_color), (300, 360)),
			call(mock_font.render(
				'-12', True, mock_color), (450, 360)),
			call(mock_font.render(
				'1', True, mock_color), (600, 360)),
			call(mock_font.render(
				'doggy', True, mock_color), (150, 390)),
			call(mock_font.render(
				'0', True, mock_color), (300, 390)),
			call(mock_font.render(
				'-1', True, mock_color), (450, 390)),
			call(mock_font.render(
				'1', True, mock_color), (600, 390)),
			call(mock_font.render(
				'paskudzio', True, mock_color), (150, 420)),
			call(mock_font.render(
				'0', True, mock_color), (300, 420)),
			call(mock_font.render(
				'-1', True, mock_color), (450, 420)),
			call(mock_font.render(
				'1', True, mock_color), (600, 420)),
			call(mock_font.render(
				'alba', True, mock_color), (150, 450)),
			call(mock_font.render(
				'0', True, mock_color), (300, 450)),
			call(mock_font.render(
				'-3', True, mock_color), (450, 450)),
			call(mock_font.render(
				'1', True, mock_color), (600, 450)),
			call(mock_font.render(
				'pablo', True, mock_color), (150, 480)),
			call(mock_font.render(
				'0', True, mock_color), (300, 480)),
			call(mock_font.render(
				'90', True, mock_color), (450, 480)),
			call(mock_font.render(
				'1', True, mock_color), (600, 480)),

		]
		mock_surface.blit.assert_has_calls(expected_calls)

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
