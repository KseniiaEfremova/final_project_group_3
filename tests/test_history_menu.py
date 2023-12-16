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
		self.history_menu = HistoryMenu(self.test_board)
		self.test_falling = FallingItemsFactory(self.test_board)
		self.test_player = Player(100, 100, self.test_board,
									self.test_falling, "Test Player")

	def test_draw_columns(self):
		mock_surface = MagicMock()
		mock_font = pygame.font.Font(None, 36)
		mock_color = (255, 255, 255)

		self.history_menu.draw_columns(mock_surface)

		expected_calls = [
			call(mock_font.render(
				'Username', True, mock_color), (100, 230)),
			call(mock_font.render(
				'Points', True, mock_color), (290, 230)),
			call(mock_font.render(
				'Life', True, mock_color), (480, 230)),
			call(mock_font.render(
				'Level', True, mock_color), (670, 230)),
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
				'Test123', True, mock_color), (100, 270)),
			call(mock_font.render(
				'-2', True, mock_color), (290, 270)),
			call(mock_font.render(
				'0', True, mock_color), (480, 270)),
			call(mock_font.render(
				'3', True, mock_color), (670, 270)),
			call(mock_font.render(
				'test', True, mock_color), (100, 300)),
			call(mock_font.render(
				'9', True, mock_color), (290, 300)),
			call(mock_font.render(
				'89', True, mock_color), (480, 300)),
			call(mock_font.render(
				'1', True, mock_color), (670, 300)),
			call(mock_font.render(
				'szam', True, mock_color), (100, 330)),
			call(mock_font.render(
				'0', True, mock_color), (290, 330)),
			call(mock_font.render(
				'90', True, mock_color), (480, 330)),
			call(mock_font.render(
				'1', True, mock_color), (670, 330)),
			call(mock_font.render(
				'gorilla', True, mock_color), (100, 360)),
			call(mock_font.render(
				'0', True, mock_color), (290, 360)),
			call(mock_font.render(
				'-12', True, mock_color), (480, 360)),
			call(mock_font.render(
				'1', True, mock_color), (670, 360)),
			call(mock_font.render(
				'doggy', True, mock_color), (100, 390)),
			call(mock_font.render(
				'0', True, mock_color), (290, 390)),
			call(mock_font.render(
				'-1', True, mock_color), (480, 390)),
			call(mock_font.render(
				'1', True, mock_color), (670, 390)),
			call(mock_font.render(
				'paskudzio', True, mock_color), (100, 420)),
			call(mock_font.render(
				'0', True, mock_color), (290, 420)),
			call(mock_font.render(
				'-1', True, mock_color), (480, 420)),
			call(mock_font.render(
				'1', True, mock_color), (670, 420)),
			call(mock_font.render(
				'alba', True, mock_color), (100, 450)),
			call(mock_font.render(
				'0', True, mock_color), (290, 450)),
			call(mock_font.render(
				'-3', True, mock_color), (480, 450)),
			call(mock_font.render(
				'1', True, mock_color), (670, 450)),
			call(mock_font.render(
				'pablo', True, mock_color), (100, 480)),
			call(mock_font.render(
				'0', True, mock_color), (290, 480)),
			call(mock_font.render(
				'90', True, mock_color), (480, 480)),
			call(mock_font.render(
				'1', True, mock_color), (670, 480)),

		]
		mock_surface.blit.assert_has_calls(expected_calls)

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('menus.history_menu.Button')
	def test_draw(self, mock_button, mock_scale, mock_load):
		mock_button.process.return_value = None
		mock_surface = pygame.Surface((800, 600))
		mock_scale.return_value = mock_surface
		mock_font = pygame.font.Font(None, 36)
		mock_font.render.return_value = pygame.Surface((200, 100))

		self.history_menu.draw()

		mock_load.assert_called_once_with(
			assets_library['backgrounds']['registration_page'])
		mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))

		mock_button_instance = mock_button.return_value
		mock_button_instance.process.assert_called_once()

	def test_back_button_handler(self):
		self.assertTrue(self.history_menu.history)

		self.history_menu.back_button_handler()

		self.assertFalse(self.history_menu.history)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
