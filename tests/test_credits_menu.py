import unittest
from unittest.mock import patch
import pygame
from board import Board
from menus.credits_menu import CreditsMenu
from utils import assets_library


class TestInstructionsMenu(unittest.TestCase):

	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.credits_menu = CreditsMenu(self.test_board)

	def test_instructions_menu_initialization(self):

		self.assertEqual(self.credits_menu.board_instance, self.test_board)
		self.assertEqual(self.credits_menu.credits, True)
		self.assertEqual(self.credits_menu.background_pic,
				assets_library['backgrounds']['credits'])

	def test_back_button_handler(self):
		self.assertTrue(self.credits_menu.credits)

		self.credits_menu.back_button_handler()

		self.assertFalse(self.credits_menu.credits)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
