import unittest
from unittest.mock import patch, MagicMock, call
import pygame
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

def tearDown(self):
	pygame.quit()
	patch.stopall()
