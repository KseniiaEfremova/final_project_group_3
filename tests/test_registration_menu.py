import unittest
from unittest.mock import patch, MagicMock
import pygame
from pygame.locals import QUIT
from db.user import *
from board import Board
from menus.registration_menu import RegistrationMenu
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.popup import PopupWindow
from utils import *


class TestRegistrationMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.registration_menu = RegistrationMenu(
			self.test_board)

	def test_registration_menu_initialization(self):
		current_image = pygame.image.load(self.registration_menu.background_pic)
		expected_image = pygame.image.load(
			assets_library['backgrounds']['registration_page'])

		current_image_str = pygame.image.tostring(
			current_image, "RGBA")
		expected_image_str = pygame.image.tostring(
			expected_image, "RGBA")

		self.assertEqual(self.registration_menu.board_instance, self.test_board)
		self.assertEqual(self.registration_menu.registration, True)
		self.assertEqual(current_image_str, expected_image_str)
		self.assertTrue(compare_instances(
			self.registration_menu.username_box, InputBox(
				250, 250, 140, 32, "",
				self.test_board)))
		self.assertTrue(compare_instances(
			self.registration_menu.password_box, InputBox(
			250, 350, 140, 32, "",
			self.test_board)))
		self.assertTrue(compare_instances(
			self.registration_menu.submit_btn, Button(
				300, 420, 200, 40, self.test_board,
				'SUBMIT', lambda: check_username_and_password(
					self.registration_menu.username_box.get_user_text(),
					self.registration_menu.password_box.get_user_text()))))
		self.assertTrue(compare_instances(
			self.registration_menu.popup_window_invalid, PopupWindow(
				800, 40, "Invalid Username or Password!")))
		self.assertTrue(compare_instances(
			self.registration_menu.popup_window_exist, PopupWindow(
			800, 40,
				"This username already exist, try another")))

	@patch('menus.registration_menu.Button')
	def test_handle_user_input(self, mock_button):
		mock_event_quit = pygame.event.Event(QUIT)
		mock_event_keydown = pygame.event.Event(pygame.KEYDOWN,
												key=pygame.K_RETURN)

		pygame.event.post(mock_event_quit)
		pygame.event.post(mock_event_keydown)

		mock_button.return_value.already_pressed = True
		self.registration_menu.submit_btn.already_pressed = (
			mock_button.return_value.already_pressed)
		self.registration_menu.process_submit = MagicMock()
		self.registration_menu.process_submit.return_value = "Test User"

		returned_username = self.registration_menu.handle_user_input()

		self.assertEqual(returned_username, "Test User")
		self.registration_menu.process_submit.assert_called_once()

	@patch('menus.registration_menu.check_username_and_password')
	@patch('menus.registration_menu.is_user_exist_in_db')
	def test_process_submit(self, mock_exist_in_db, mock_check_credentials):
		mock_check_credentials.return_value = ("Test User", "Test123!")
		self.registration_menu.check_username_and_password = (
			mock_check_credentials.return_value)
		mock_exist_in_db.return_value = False
		self.registration_menu.is_user_exist_in_db = mock_exist_in_db
		actual_username = self.registration_menu.process_submit()

		self.assertEqual(actual_username, "Test User")

		mock_check_credentials.return_value = None
		self.registration_menu.check_username_and_password = (
			mock_check_credentials.return_value)
		actual_username = self.registration_menu.process_submit()

		self.assertEqual(actual_username, None)

	@patch('pygame.display.update')
	@patch('menus.registration_menu.PopupWindow')
	def test_handle_invalid_credentials(self, mock_popup, mock_update):
		mock_popup.return_value = PopupWindow(
            800, 40, "Invalid Username or Password!")
		self.registration_menu.handle_invalid_credentials()

		mock_update.assert_called_once()
		self.assertTrue(mock_popup.opened)

	@patch('pygame.display.update')
	@patch('menus.registration_menu.PopupWindow')
	@patch('menus.registration_menu.is_user_exist_in_db')
	@patch('menus.registration_menu.add_valid_user_data_to_db')
	def test_handle_valid_credentials(
			self, mock_add_user, mock_exist_in_db, mock_popup, mock_update):
		mock_exist_in_db.return_value = True
		mock_popup.return_value = PopupWindow(
            800, 40,
            "This username already exist, try another")

		actual_username = self.registration_menu.handle_valid_credentials(
			("Test User", "Test123!"))

		self.assertTrue(mock_popup.opened)
		mock_update.assert_called_once()
		self.assertEqual(actual_username, None)

		mock_exist_in_db.return_value = False
		self.registration_menu.is_user_exist_in_db = mock_exist_in_db

		actual_username = self.registration_menu.handle_valid_credentials(
			("Test User", "Test123!"))

		self.assertEqual(actual_username, "Test User")
		mock_add_user.assert_called_once()

	@patch('db.user.add_valid_user_data_to_db')
	def test_add_user_to_db(self, mock_add_user):
		mock_add_user.return_value = "Test User", "Test123!"

		actual_username = self.registration_menu.add_user_to_db(
			"Test User", "Test123!")
		expected_username, _ = mock_add_user.return_value

		self.assertEqual(actual_username, expected_username)

	@patch('menus.registration_menu.PopupWindow')
	def test_finish_registration(self, mock_popup):
		self.registration_menu.finish_registration()

		self.assertFalse(self.registration_menu.registration)
		self.assertFalse(self.registration_menu.submit_btn.one_press)

	@patch('pygame.display.update')
	def test_switch_to_main_background(self, mock_update):

		self.registration_menu.switch_to_main_background()

		actual_image = pygame.image.tostring(
			self.registration_menu.board_instance.image, "RGBA")
		expected_image = pygame.image.tostring(
			pygame.transform.scale(pygame.image.load(
			assets_library['backgrounds']['main_background']),
				(800, 600)), "RGBA")

		mock_update.assert_called_once()
		self.assertEqual(actual_image, expected_image)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
