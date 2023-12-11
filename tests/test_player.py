import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.falling_items.points_falling_item import *
from models.falling_items.damage_falling_item import *
from utils import assets_library


class TestPlayer(unittest.TestCase):
	def setUp(self):
		pygame.init()
		self.board = pygame.display.set_mode((800, 600))
		self.test_board = Board("Test Board", (800, 600), 60)
		self.test_group = FallingItemsFactory(self.test_board)
		self.player = Player(100, 100, self.test_board, self.test_group,
						"Test Player")

	def test_player_initialization(self):
		player = Player(100, 100, self.test_board, self.test_group, "Test Player")

		self.assertEqual(self.player.rect.center, (100, 100))
		self.assertEqual(player.width, 100)
		self.assertEqual(player.height, 238)

	def test_draw_player(self):
		self.player.draw_player()
		self.player = pygame.surfarray.array3d(self.player.image)
		loaded_player = pygame.image.load(assets_library['sprites']['player']['player_right']['player_right1'])
		loaded_player = pygame.transform.scale(loaded_player, (100, 238))
		player_content = pygame.surfarray.array3d(loaded_player)
		diff = np.abs(player_content - self.player)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

	# TODO: check out how to test movement to the left and right
	# @patch('models.player.pygame.key.get_pressed')
	# def test_player_movement(self, mock_get_pressed):
	# 	initial_x = self.player.rect.x
	# 	self.player.move()
	# 	self.assertEqual(self.player.rect.x, initial_x - 10)
	# 	self.player.animate.assert_called_once_with('left')

	@patch('models.player.pygame.key.get_pressed')
	def test_boundary_checking(self, mock_get_pressed):
		self.player.rect.x = 0
		self.player.move()
		self.assertEqual(self.player.rect.x, 10)
		self.player.rect.x = self.test_board.res[0] - self.player.width
		self.player.move()
		expected_x = self.test_board.res[0] - self.player.width
		self.assertEqual(self.player.rect.x, expected_x)

	def test_animate_right(self):
		initial_sprite = self.player.current_sprite
		initial_image = self.player.image

		self.player.animate('right')

		self.assertEqual(self.player.current_sprite, (
					initial_sprite + 1) % 8)
		self.assertNotEqual(self.player.image, initial_image)

	def test_animate_left(self):
		initial_sprite = self.player.current_sprite
		initial_image = self.player.image

		self.player.animate('left')

		self.assertEqual(self.player.current_sprite, (
					initial_sprite + 1) % 8)
		self.assertNotEqual(self.player.image, initial_image)

	def test_points_collision_python(self):
		python = PythonItem("Python", self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.points_collision(python)
		self.assertEqual(self.player.points, initial_points + python.points)
		self.assertEqual(self.player.life, initial_life + python.damage)

	def test_points_collision_tick(self):
		tick = TickItem("Tick", self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.points_collision(tick)
		self.assertEqual(self.player.points, initial_points + tick.points)
		self.assertEqual(self.player.life, initial_life + tick.damage)

	def test_points_collision_duck(self):
		duck = RubberDuckItem("Duck", self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.points_collision(duck)
		self.assertEqual(self.player.points, initial_points + duck.points)
		self.assertEqual(self.player.life, initial_life + duck.damage)

	def test_damage_collision_warning(self):
		image = pygame.Surface((50, 50))
		warning = WarningItem(image, self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.damage_collision(warning)
		self.assertEqual(self.player.points, initial_points - warning.points)
		self.assertEqual(self.player.life, initial_life - warning.damage)

	def test_damage_collision_error(self):
		image = pygame.Surface((50, 50))
		error = ErrorItem(image, self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.damage_collision(error)
		self.assertEqual(self.player.points, initial_points - error.points)
		self.assertEqual(self.player.life, initial_life - error.damage)

	def test_damage_collision_bug(self):
		image = pygame.Surface((50, 50))
		bug = BugItem(image, self.test_board)
		initial_points = self.player.points
		initial_life = self.player.life
		self.player.damage_collision(bug)
		self.assertEqual(self.player.points, initial_points - bug.points)
		self.assertEqual(self.player.life, initial_life - bug.damage)

def tearDown(self):
		pygame.quit()
		patch.stopall()
