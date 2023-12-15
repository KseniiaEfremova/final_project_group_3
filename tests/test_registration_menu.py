import unittest
from unittest.mock import patch, Mock
import pygame
from pygame.locals import QUIT
from db.user import *
from board import Board
from menus.registration_menu import RegistrationMenu
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.text_drawer import TextDrawer
from models.components.popup import PopupWindow
from utils import assets_library


def compare_instances(actual, expected):
	return actual.get_attributes() == expected.get_attributes()


class TestRegistrationMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.registration_menu = RegistrationMenu(
			self.test_board)

	def test_registration_menu_initialization(self):
		current_image = self.registration_menu.background_image
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


@patch('pygame.image.load')
@patch('pygame.transform.scale')
@patch('menus.registration_menu.Button')
@patch('menus.registration_menu.TextDrawer')
@patch('menus.registration_menu.InputBox')
@patch('menus.registration_menu.PopupWindow')
def test_draw(self, mock_popup, mock_input_box, mock_text_drawer, mock_button, mock_scale, mock_load):
	mock_surface = pygame.Surface((800, 600))
	mock_scale.return_value = mock_surface
	mock_button.return_value.process.return_value = None
	mock_font = pygame.font.Font(None, 36)
	mock_font.render.return_value = pygame.Surface((200, 100))

	self.history_menu.draw()

	mock_load.assert_called_once_with(
		assets_library['backgrounds']['registration_page'])
	mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))

	mock_button.assert_called_once_with(
		300, 420, 200, 40, self.registration_menu.board_instance, 'SUBMIT')
	mock_button_instance = mock_button.return_value
	mock_button_instance.process.assert_called_once()

	mock_text_drawer.assert_called_with("Enter your username: ", (255, 255, 255),
            100, 220, mock_font)
	mock_text_drawer.assert_called_with("Enter your password: ", (255, 255, 255),
            100, 320, mock_font)

	mock_input_box.assert_called(2)

	mock_popup.assert_not_called()

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	@patch('pygame.display.update')
	@patch('menus.registration_menu.Button')
	@patch('menus.registration_menu.TextDrawer')
	@patch('menus.registration_menu.InputBox')
	@patch('menus.registration_menu.PopupWindow')
	def test_process_registration(self, mock_popup, mock_input_box, mock_text_drawer,
				  mock_button, mock_update, mock_scale, mock_load):
		mock_surface = pygame.Surface((800, 600))
		mock_scale.return_value = mock_surface
		mock_button.return_value.process.return_value = None
		mock_font = pygame.font.Font(None, 36)
		mock_font.render.return_value = pygame.Surface((200, 100))
		self.registration_menu.handle_user_input.return_value = "Test User"

		returned_username = self.registration_menu.process_registration()

		mock_update.assert_called_once()
		self.assertEqual(returned_username, "Test User")


@patch('menus.registration_menu.Button')
def test_handle_user_input(self, mock_button):
	mock_event_quit = pygame.event.Event(QUIT)
	mock_event_keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)

	pygame.event.post(mock_event_quit)
	pygame.event.post(mock_event_keydown)

	mock_button.return_value.alreadyPressed = True
	self.registration_menu.process_submit = Mock(return_value="Test User")

	returned_username = self.registration_menu.handle_user_input()

	self.assertEqual(returned_username, "Test User")
	mock_button.return_value.process_submit.assert_called_once()


@patch('menus.registration_menu.handle_invalid_credentials')
@patch('menus.registration_menu.handle_valid_credentials')
@patch('menus.registration_menu.check_username_and_password')
def test_process_submit(self, mock_check_credentials, mock_handle_valid, mock_handle_invalid):
	expected_username = mock_handle_valid.return_value
	mock_check_credentials.return_value = ("Test User", "Test123!")

	returned_username = self.registration_menu.process_submit()

	mock_handle_valid.assert_called_once_with(mock_check_credentials.return_value)
	mock_handle_invalid.assert_not_called()
	self.assertEqual(returned_username, expected_username)

	mock_check_credentials.return_value = None

	self.registration_menu.process_submit()

	mock_handle_invalid.assert_called_once()
	mock_handle_valid.assert_not_called()


def tearDown(self):
	pygame.quit()
	patch.stopall()
