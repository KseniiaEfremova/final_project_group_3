import unittest
from unittest.mock import patch
import pygame
from board import Board
from menus.instructions_menu import InstructionsMenu
from utils import assets_library

def compare_instances(actual, expected):
	return actual.get_attributes() == expected.get_attributes()

class TestInstructionsMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.instructions_menu = InstructionsMenu(self.test_board)

	def test_instructions_menu_initialization(self):

		self.assertEqual(self.instructions_menu.board_instance, self.test_board)
		self.assertEqual(self.instructions_menu.instructions, True)
		self.assertEqual(self.instructions_menu.background_pic,
				assets_library['backgrounds']['instructions'])

	def test_back_button_handler(self):
		self.assertTrue(self.instructions_menu.instructions)

		self.instructions_menu.back_button_handler()

		self.assertFalse(self.instructions_menu.instructions)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
