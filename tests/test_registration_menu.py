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

	# @patch('menus.registration_menu.pygame.display.update')
	# @patch('menus.registration_menu.pygame.transform.scale')
	# def test_process_registration(self, mock_scale, mock_update):
	# 	mock_popup_invalid = MagicMock()
	# 	mock_popup_exist = MagicMock()
	# 	mock_popup_invalid.opened = True
	# 	mock_popup_exist.opened = False
	# 	mock_scale.return_value = pygame.Surface((800, 600))
	#
	# 	self.registration_menu.process_registration()
	#
	# 	mock_scale.assert_called_once_with(
	# 		self.registration_menu.background_image, (800, 600))
	# 	self.registration_menu.draw.assert_called_once()
	# 	mock_popup_invalid.draw_window.assert_called_once_with(
	# 		self.test_board.board)
	# 	mock_update.assert_called_once()
	# 	self.registration_menu.handle_user_input.assert_called_once()

#
# @patch('pygame.image.load')
# @patch('pygame.transform.scale')
# @patch('menus.history_menu.Button')
# def test_draw(self, mock_button, mock_scale, mock_load):
# 	mock_button.return_value.process.return_value = None
# 	mock_surface = pygame.Surface((800, 600))
# 	mock_scale.return_value = mock_surface
# 	mock_font = pygame.font.Font(None, 36)
# 	mock_font.render.return_value = pygame.Surface((200, 100))
#
# 	self.history_menu.draw()
#
# 	mock_load.assert_called_once_with(
# 		assets_library['backgrounds']['registration_page'])
# 	mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))
#
# 	mock_button.assert_called_once_with(
# 		20, 10, 200, 40, self.history_menu.board_instance, 'BACK TO MENU')
# 	mock_button_instance = mock_button.return_value
# 	mock_button_instance.process.assert_called_once()
#
def tearDown(self):
	pygame.quit()
	patch.stopall()
