import unittest
from unittest.mock import patch
import pygame
import numpy as np
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory


class TestPlayer(unittest.TestCase):
	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.test_group = FallingItemsFactory(self.test_board)

	def test_player_initialization(self):
		player = Player(100, 100, self.test_board, self.test_group)

		self.assertEqual(player.rect.center, (100, 100))
		self.assertEqual(player.width, 100)
		self.assertEqual(player.height, 90)

	def test_draw_player(self):
		player = Player(100, 100, self.test_board, self.test_group)
		player.draw_player()
		player = pygame.surfarray.array3d(player.image)
		loaded_player = pygame.image.load("assets/sprites/player_idle.png")
		loaded_player = pygame.transform.scale(loaded_player, (100, 238))
		player_content = pygame.surfarray.array3d(loaded_player)
		diff = np.abs(player_content - player)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)


	# TODO: this is causing import errors, check out why
	# @patch('player.pygame.key.get_pressed')
	# def test_player_movement(self, mock_get_pressed):
	# 	self.player = Player(100, 100, self.test_board, self.test_group)
	# 	initial_x = self.player.rect.x
	# 	# check why this move is only to the right
	# 	self.player.move()
	# 	self.assertEqual(self.player.rect.x, initial_x + 10)
	#
	# @patch('player.pygame.key.get_pressed')
	# def test_boundary_checking(self, mock_get_pressed):
	# 	self.player = Player(100, 100, self.test_board, self.test_group)
	# 	self.player.rect.x = 0
	# 	self.player.move()
	# 	self.assertEqual(self.player.rect.x, 10)
	# 	self.player.rect.x = self.test_board.res[0] - self.player.width
	# 	self.player.move()
	# 	expected_x = self.test_board.res[0] - self.player.width
	# 	self.assertEqual(self.player.rect.x, expected_x)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
