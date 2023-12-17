import unittest
from unittest.mock import patch, MagicMock
import pygame
from board import Board
from menus.end_game_menu import EndGameMenu
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.player import Player
from utils import assets_library


class TestEndGameMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.win_menu = EndGameMenu(
			self.test_board, assets_library['backgrounds']['win'])
		self.game_over_menu = EndGameMenu(
			self.test_board, assets_library['backgrounds']['game_over'])
		self.test_falling = FallingItemsFactory(self.test_board)
		self.test_player = Player(
			100, 100, self.test_board, self.test_falling,
			"Test Player")

	def test_win_menu_initialization(self):

		self.assertEqual(self.win_menu.board_instance, self.test_board)
		self.assertEqual(self.win_menu.play_again, False)
		self.assertEqual(
			self.win_menu.background_pic, assets_library['backgrounds']['win'])

	def test_game_over_menu_initialization(self):

		self.assertEqual(self.game_over_menu.board_instance, self.test_board)
		self.assertEqual(self.game_over_menu.play_again, False)
		self.assertEqual(
			self.game_over_menu.background_pic,
			assets_library['backgrounds']['game_over'])

	def test_get_play_again(self):

		self.assertFalse(self.win_menu.play_again)
		self.assertFalse(self.game_over_menu.play_again)

	def test_play_again_handler(self):
		self.assertFalse(self.win_menu.play_again)

		self.win_menu.play_again_handler()

		self.assertTrue(self.win_menu.play_again)

	@patch('pygame.quit')
	@patch('sys.exit')
	def test_exit_game_handler(self, mock_sys_exit, mock_pygame_quit):
		with patch('pygame.event.get',
				   return_value=[MagicMock(type=pygame.QUIT)]):
			self.win_menu.exit_game_handler()
			mock_pygame_quit.assert_called_once()
			mock_sys_exit.assert_called_once()

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('menus.end_game_menu.Button')
	def test_draw(self, mock_button, mock_scale, mock_load):

		mock_button.return_value.process.return_value = None
		mock_surface = pygame.Surface((800, 600))
		mock_scale.return_value = mock_surface

		self.win_menu.draw()

		mock_load.assert_called_once_with(
			assets_library['backgrounds']['win'])
		mock_scale.assert_called_once_with(mock_load.return_value, (
			self.win_menu.width, self.win_menu.height))
		mock_button.assert_any_call(200, 500, 150, 40, self.test_board,
									'Play again',
									self.win_menu.play_again_handler, False)
		mock_button.assert_any_call(450, 500, 150, 40, self.test_board, 'Exit',
									self.win_menu.exit_game_handler, False)
		self.assertEqual(mock_button.call_count, 2)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
