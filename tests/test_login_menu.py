import unittest
from unittest.mock import patch, MagicMock
import pygame
from pygame.locals import QUIT
from db.user import *
from board import Board
from menus.login_menu import LoginMenu
from models.components.button import Button
from models.components.input_box import InputBox
from models.components.text_drawer import TextDrawer
from models.components.popup import PopupWindow
from utils import assets_library


def compare_instances(actual, expected):
	return actual.get_attributes() == expected.get_attributes()


class TestLoginMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		pygame.font.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.login_menu = LoginMenu(self.test_board)

	def test_login_menu_initialization(self):
		current_image = pygame.image.load(self.login_menu.background_pic)
		expected_image = pygame.image.load(
			assets_library['backgrounds']['registration_page'])

		current_image_str = pygame.image.tostring(
			current_image, "RGBA")
		expected_image_str = pygame.image.tostring(
			expected_image, "RGBA")

		self.assertEqual(self.login_menu.board_instance, self.test_board)
		self.assertEqual(self.login_menu.login, True)
		self.assertEqual(current_image_str, expected_image_str)
		self.assertTrue(compare_instances(
			self.login_menu.username_box, InputBox(
				250, 250, 140, 32, "",
				self.test_board)))
		self.assertTrue(compare_instances(
			self.login_menu.password_box, InputBox(
				250, 350, 140, 32, "",
				self.test_board)))
		self.assertTrue(compare_instances(
			self.login_menu.submit_btn, Button(
				300, 450, 200, 40, self.test_board,
				'SUBMIT', lambda: check_username_and_password(
					self.login_menu.username_box.get_user_text(),
					self.login_menu.password_box.get_user_text()))))
		# self.assertTrue(compare_instances(self.login_menu.back_btn, Button(
		# 	0, 560, 200, 40, self.test_board,
		# 	'BACK TO MENU', self.login_menu.handle_back_to_menu)))
		self.assertTrue(compare_instances(
			self.login_menu.popup_window_incorrect, PopupWindow(
				800, 40, "Incorrect Username or Password!")))

	def test_handle_back_to_menu(self):
		self.assertTrue(self.login_menu.login)

		self.login_menu.handle_back_to_menu()

		self.assertFalse(self.login_menu.login)

	@patch('pygame.image.load')
	@patch('pygame.transform.scale')
	def test_draw(self, mock_scale, mock_load):
		mock_surface = pygame.Surface((800, 600))
		mock_scale.return_value = mock_surface

		mock_font = pygame.font.Font(assets_library['fonts']['kiddy_play'], 30)
		mock_font.render.return_value = pygame.Surface((200, 100))
		self.login_menu.text_drawer = MagicMock()
		self.login_menu.popup_window_incorrect = MagicMock()
		self.login_menu.password_box = MagicMock()
		self.login_menu.username_box = MagicMock()
		self.login_menu.submit_btn = MagicMock()
		self.login_menu.submit_btn.process.return_value = None
		self.login_menu.back_btn = MagicMock()
		self.login_menu.back_btn.process.return_value = None

		self.login_menu.draw()

		mock_load.assert_called_once_with(
			assets_library['backgrounds']['registration_page'])
		mock_scale.assert_called_once_with(mock_load.return_value, (800, 600))

		self.login_menu.submit_btn.process.assert_called_once()
		self.login_menu.back_btn.process.assert_called_once()

		self.assertEqual(self.login_menu.text_drawer.draw_text.call_count, 3)
		self.login_menu.text_drawer.draw_text.assert_called_with(
			"Password: ", (255, 255, 255), 100, 320, mock_font)

		self.login_menu.popup_window_incorrect.draw_window.assert_called_once()

		self.login_menu.username_box.draw_box.assert_called_once()
		self.login_menu.password_box.draw_box.assert_called_once()

	def test_process_login(self):
		self.login_menu.draw = MagicMock()
		self.login_menu.handle_user_input = MagicMock()
		self.login_menu.handle_user_input.return_value = "Test User"

		returned_username = self.login_menu.process_login()

		self.login_menu.draw.assert_called_once()
		self.assertEqual(returned_username, "Test User")

	@patch('menus.login_menu.Button')
	def test_handle_user_input(self, mock_button):
		mock_event_quit = pygame.event.Event(QUIT)
		mock_event_keydown = pygame.event.Event(pygame.KEYDOWN,
												key=pygame.K_RETURN)

		pygame.event.post(mock_event_quit)
		pygame.event.post(mock_event_keydown)

		mock_button.return_value.alreadyPressed = True
		self.login_menu.submit_btn.alreadyPressed = mock_button.return_value.alreadyPressed
		self.login_menu.process_submit = MagicMock()
		self.login_menu.process_submit.return_value = "Test User"

		returned_username = self.login_menu.handle_user_input()

		self.assertEqual(returned_username, "Test User")
		self.login_menu.process_submit.assert_called_once()

	@patch('menus.login_menu.check_passwords')
	@patch('menus.login_menu.is_user_exist_in_db')
	def test_process_submit(self, mock_exist_in_db, mock_check_passwords):
		mock_check_passwords.return_value = True
		self.login_menu.check_username_and_password = mock_check_passwords.return_value
		mock_exist_in_db.return_value = True
		self.login_menu.is_user_exist_in_db = mock_exist_in_db
		self.login_menu.username_box.get_user_text = MagicMock()
		self.login_menu.username_box.get_user_text.return_value = "Test User"
		actual_username = self.login_menu.process_submit()

		self.assertEqual(actual_username, "Test User")

		mock_check_passwords.return_value = False
		actual_username = self.login_menu.process_submit()

		self.assertTrue(actual_username, '')

	@patch('menus.login_menu.PopupWindow')
	def test_handle_incorrect_credentials(self, mock_popup):
		mock_popup.return_value = PopupWindow(
			800, 40, "Incorrect Username or Password!")

		self.login_menu.handle_incorrect_credentials()

		self.assertTrue(mock_popup.opened)

	def test_handle_correct_credentials(self):
		self.login_menu.finish_login = MagicMock()

		self.login_menu.handle_correct_credentials()

		self.assertFalse(self.login_menu.popup_window_incorrect.opened)
		self.login_menu.finish_login.assert_called_once()

	def test_finish_login(self):
		self.login_menu.switch_to_main_background = MagicMock()

		self.login_menu.finish_login()

		self.assertFalse(self.login_menu.login)
		self.assertFalse(self.login_menu.submit_btn.onePress)
		self.assertFalse(self.login_menu.popup_window_incorrect.opened)
		self.login_menu.switch_to_main_background.assert_called_once()


	@patch('pygame.display.update')
	def test_switch_to_main_background(self, mock_update):

		self.login_menu.switch_to_main_background()

		actual_image = pygame.image.tostring(self.login_menu.board_instance.image, "RGBA")
		expected_image = pygame.image.tostring(pygame.transform.scale(pygame.image.load(
			assets_library['backgrounds']['main_background']), (800, 600)), "RGBA")

		mock_update.assert_called_once()
		self.assertEqual(actual_image, expected_image)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
