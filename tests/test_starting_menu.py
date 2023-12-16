import unittest
from unittest.mock import patch, MagicMock
import pygame
from board import Board
from menus.starting_menu import StartingMenu
from menus.registration_menu import RegistrationMenu
from menus.credits_menu import CreditsMenu
from menus.history_menu import HistoryMenu
from menus.instructions_menu import InstructionsMenu
from models.components.button import Button
from utils import assets_library


def compare_instances(actual, expected):
	return actual.get_attributes() == expected.get_attributes()


class TestStartingMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.starting_menu = StartingMenu(
			self.test_board)

	def test_starting_menu_initialization(self):
		current_image = pygame.image.load(self.starting_menu.background_pic)
		expected_image = pygame.image.load(
			assets_library['backgrounds']['registration_page'])

		current_image_str = pygame.image.tostring(
			current_image, "RGBA")
		expected_image_str = pygame.image.tostring(
			expected_image, "RGBA")

		self.assertEqual(self.starting_menu.board_instance, self.test_board)
		self.assertEqual(current_image_str, expected_image_str)
		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.registration)
		self.assertFalse(self.starting_menu.login)
		self.assertFalse(self.starting_menu.history)
		self.assertFalse(self.starting_menu.instructions)
		self.assertFalse(self.starting_menu.credits)
		self.assertTrue(compare_instances(
			self.starting_menu.registration_button, Button(
				300, 250, 200, 40, self.test_board,
				'Registration', self.starting_menu.register_handler)))
		self.assertTrue(compare_instances(
			self.starting_menu.login_button, Button(
				300, 300, 200, 40, self.test_board,
				'Login', self.starting_menu.login_handler)))
		self.assertTrue(compare_instances(
			self.starting_menu.history_button, Button(
				300, 350, 200, 40, self.test_board,
				'History', self.starting_menu.history_handler)))
		self.assertTrue(compare_instances(
			self.starting_menu.instructions_button, Button(
				300, 400, 200, 40, self.test_board,
				'Instructions', self.starting_menu.instructions_handler)))
		self.assertTrue(compare_instances(
			self.starting_menu.credits_button, Button(
				300, 450, 200, 40, self.test_board,
				'Credits', self.starting_menu.credits_handler)))

	def test_register_handler(self):

		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.registration)

		self.starting_menu.register_handler()

		self.assertFalse(self.starting_menu.is_open)
		self.assertTrue(self.starting_menu.registration)


	def test_login_handler(self):
		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.login)

		self.starting_menu.login_handler()

		self.assertFalse(self.starting_menu.is_open)
		self.assertTrue(self.starting_menu.login)



	def test_history_handler(self):
		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.history)

		self.starting_menu.history_handler()

		self.assertFalse(self.starting_menu.is_open)
		self.assertTrue(self.starting_menu.history)



	def test_instructions_handler(self):
		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.instructions)

		self.starting_menu.instructions_handler()

		self.assertFalse(self.starting_menu.is_open)
		self.assertTrue(self.starting_menu.instructions)

	def test_credits_handler(self):
		self.assertTrue(self.starting_menu.is_open)
		self.assertFalse(self.starting_menu.credits)

		self.starting_menu.credits_handler()

		self.assertFalse(self.starting_menu.is_open)
		self.assertTrue(self.starting_menu.credits)

	def test_reset_flags(self):
		self.starting_menu.reset_flags()

		self.assertFalse(self.starting_menu.registration)
		self.assertFalse(self.starting_menu.login)
		self.assertFalse(self.starting_menu.credits)
		self.assertFalse(self.starting_menu.history)
		self.assertFalse(self.starting_menu.instructions)

	def test_show_credits_menu(self):
		mock_credits = MagicMock(spec=CreditsMenu)

		self.starting_menu.show_credits_menu(mock_credits)

		self.assertFalse(self.starting_menu.is_open)
		mock_credits.draw.assert_called_once()

	def test_show_history_menu(self):
		mock_history = MagicMock(spec=HistoryMenu)

		self.starting_menu.show_history_menu(mock_history)

		self.assertFalse(self.starting_menu.is_open)
		mock_history.draw.assert_called_once()

	def test_show_instructions_menu(self):
		mock_instructions = MagicMock(spec=InstructionsMenu)

		self.starting_menu.show_history_menu(mock_instructions)

		self.assertFalse(self.starting_menu.is_open)
		mock_instructions.draw.assert_called_once()

	def tearDown(self):
		pygame.quit()
		patch.stopall()
