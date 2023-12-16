import unittest
from unittest.mock import patch, MagicMock
import pygame
from pygame.locals import QUIT
from db.user import *
from board import Board
from menus.starting_menu import StartingMenu
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.text_drawer import TextDrawer
from models.components.popup import PopupWindow
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

	# @patch('menus.starting_menu.pygame.image.load')
	# @patch('menus.starting_menu.pygame.transform.scale')
	# def test_draw(self, mock_scale, mock_load):
	# 	mock_surface = pygame.Surface((800, 600))
	# 	mock_scale.return_value = mock_surface
	#
	# 	mock_font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)
	# 	mock_font.render.return_value = pygame.Surface((200, 100))
		# self.registration_menu.text_drawer = MagicMock()
		# self.registration_menu.popup_window_invalid = MagicMock()
		# self.registration_menu.popup_window_exist = MagicMock()
		# self.registration_menu.password_box = MagicMock()
		# self.registration_menu.username_box = MagicMock()
		# self.registration_menu.submit_btn = MagicMock()
		# self.registration_menu.submit_btn.process.return_value = None
		# print('failing from starting menu')
		# self.starting_menu.draw()

		# mock_load.assert_called_once_with(
		# 	assets_library['backgrounds']['registration_page'])
		# mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))
		#
		# self.registration_menu.submit_btn.process.assert_called_once()
		#
		# self.assertEqual(self.registration_menu.text_drawer.draw_text.call_count, 3)
		# self.registration_menu.text_drawer.draw_text.assert_called_with(
		# 	"Enter your password: ", (255, 255, 255), 100, 320, mock_font)
		#
		# self.registration_menu.popup_window_invalid.draw_window.assert_called_once()
		# self.registration_menu.popup_window_exist.draw_window.assert_called_once()
		#
		# self.registration_menu.username_box.draw_box.assert_called_once()
		# self.registration_menu.password_box.draw_box.assert_called_once()

	# @patch('pygame.image.load')
	# @patch('pygame.transform.scale')
	# @patch('pygame.display.update')
	# def test_process_registration(
	# 		self, mock_update, mock_scale, mock_load):
	# 	mock_surface = pygame.Surface((800, 600))
	# 	mock_scale.return_value = mock_surface
	# 	self.registration_menu.submit_btn = MagicMock()
	# 	self.registration_menu.submit_btn.process.return_value = None
	# 	mock_font = pygame.font.Font(None, 36)
	# 	mock_font.render.return_value = pygame.Surface((200, 100))
	# 	self.registration_menu.handle_user_input = MagicMock()
	# 	self.registration_menu.handle_user_input.return_value = "Test User"
	#
	# 	returned_username = self.registration_menu.process_registration()
	#
	# 	self.assertEqual(mock_update.call_count, 2)
	# 	self.assertEqual(returned_username, "Test User")
	#
	# @patch('menus.registration_menu.Button')
	# def test_handle_user_input(self, mock_button):
	# 	mock_event_quit = pygame.event.Event(QUIT)
	# 	mock_event_keydown = pygame.event.Event(pygame.KEYDOWN,
	# 											key=pygame.K_RETURN)
	#
	# 	pygame.event.post(mock_event_quit)
	# 	pygame.event.post(mock_event_keydown)
	#
	# 	mock_button.return_value.alreadyPressed = True
	# 	self.registration_menu.submit_btn.alreadyPressed = mock_button.return_value.alreadyPressed
	# 	self.registration_menu.process_submit = MagicMock()
	# 	self.registration_menu.process_submit.return_value = "Test User"
	#
	# 	returned_username = self.registration_menu.handle_user_input()
	#
	# 	self.assertEqual(returned_username, "Test User")
	# 	self.registration_menu.process_submit.assert_called_once()
	#
	# @patch('menus.registration_menu.check_username_and_password')
	# @patch('menus.registration_menu.is_user_exist_in_db')
	# def test_process_submit(self, mock_exist_in_db, mock_check_credentials):
	# 	mock_check_credentials.return_value = ("Test User", "Test123!")
	# 	self.registration_menu.check_username_and_password = mock_check_credentials.return_value
	# 	mock_exist_in_db.return_value = False
	# 	self.registration_menu.is_user_exist_in_db = mock_exist_in_db
	# 	actual_username = self.registration_menu.process_submit()
	#
	# 	self.assertEqual(actual_username, "Test User")
	#
	# 	mock_check_credentials.return_value = None
	# 	self.registration_menu.check_username_and_password = mock_check_credentials.return_value
	# 	actual_username = self.registration_menu.process_submit()
	#
	# 	self.assertEqual(actual_username, None)
	#
	# @patch('pygame.display.update')
	# @patch('menus.registration_menu.PopupWindow')
	# def test_handle_invalid_credentials(self, mock_popup, mock_update):
	# 	mock_popup.return_value = PopupWindow(
    #         800, 40, "Invalid Username or Password!")
	# 	self.registration_menu.handle_invalid_credentials()
	#
	# 	mock_update.assert_called_once()
	# 	self.assertTrue(mock_popup.opened)
	#
	# @patch('pygame.display.update')
	# @patch('menus.registration_menu.PopupWindow')
	# @patch('menus.registration_menu.is_user_exist_in_db')
	# @patch('menus.registration_menu.add_valid_user_data_to_db')
	# def test_handle_valid_credentials(
	# 		self, mock_add_user, mock_exist_in_db, mock_popup, mock_update):
	# 	mock_exist_in_db.return_value = True
	# 	mock_popup.return_value = PopupWindow(
    #         800, 40,
    #         "This username already exist, try another")
	#
	# 	actual_username = self.registration_menu.handle_valid_credentials(
	# 		("Test User", "Test123!"))
	#
	# 	self.assertTrue(mock_popup.opened)
	# 	mock_update.assert_called_once()
	# 	self.assertEqual(actual_username, None)
	#
	# 	mock_exist_in_db.return_value = False
	# 	self.registration_menu.is_user_exist_in_db = mock_exist_in_db
	#
	# 	actual_username = self.registration_menu.handle_valid_credentials(
	# 		("Test User", "Test123!"))
	#
	# 	self.assertEqual(actual_username, "Test User")
	# 	mock_add_user.assert_called_once()
	#
	# @patch('db.user.add_valid_user_data_to_db')
	# def test_add_user_to_db(self, mock_add_user):
	# 	mock_add_user.return_value = "Test User", "Test123!"
	#
	# 	actual_username = self.registration_menu.add_user_to_db("Test User",
	# 															"Test123!")
	# 	expected_username, _ = mock_add_user.return_value
	#
	# 	self.assertEqual(actual_username, expected_username)
	#
	# @patch('menus.registration_menu.PopupWindow')
	# def test_finish_registration(self, mock_popup):
	# 	self.registration_menu.finish_registration()
	#
	# 	self.assertFalse(self.registration_menu.registration)
	# 	self.assertFalse(self.registration_menu.submit_btn.onePress)
	#
	# @patch('pygame.display.update')
	# def test_switch_to_main_background(self, mock_update):
	#
	# 	self.registration_menu.switch_to_main_background()
	#
	# 	actual_image = pygame.image.tostring(self.registration_menu.board_instance.image, "RGBA")
	# 	expected_image = pygame.image.tostring(pygame.transform.scale(pygame.image.load(
	# 		assets_library['backgrounds']['main_background']), (800, 600)), "RGBA")
	#
	# 	mock_update.assert_called_once()
	# 	self.assertEqual(actual_image, expected_image)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
