import unittest
from unittest.mock import patch
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

		self.assertEqual(self.player.rect.center, (100, 100))
		self.assertEqual(self.player.width, 100)
		self.assertEqual(self.player.height, 238)

	def test_draw_player(self):
		self.player.draw_player()
		self.player = pygame.surfarray.array3d(self.player.image)
		loaded_player = pygame.image.load(
			assets_library['sprites']['player']['player_right']['player_right1'])
		loaded_player = pygame.transform.scale(loaded_player, (100, 238))
		player_content = pygame.surfarray.array3d(loaded_player)
		diff = np.abs(player_content - self.player)
		total_diff = np.sum(diff)
		allowable_diff = 0

		self.assertLessEqual(total_diff, allowable_diff)

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

	def test_get_lives(self):
		self.assertEqual(self.player.life, 90)

	def test_get_points(self):
		self.assertEqual(self.player.points, 0)

	def test_get_level(self):
		self.assertEqual(self.player.level, 1)

	def test_get_is_winner(self):
		self.assertEqual(self.player.is_winner, False)

	def test_get_is_loser(self):
		self.assertEqual(self.player.is_loser, False)

	def test_check_is_winner_success(self):
		self.player.life = 90
		self.player.level = 3
		self.player.check_is_winner()

		self.assertEqual(self.player.is_winner, True)

	def test_check_is_winner_fail(self):
		self.player.life = -10
		self.player.level = 3
		self.player.check_is_winner()

		self.assertEqual(self.player.is_winner, False)

	def test_toggle_is_winner(self):
		self.player.toggle_is_winner()

		self.assertEqual(self.player.is_winner, True)

	def test_toggle_is_loser(self):
		self.player.toggle_is_loser()

		self.assertEqual(self.player.is_loser, True)

	def test_check_for_level_up(self):
		self.player.check_for_level_up()

		self.assertEqual(self.player.leveled_up, True)

	def test_level_up_player(self):
		self.player.level_up_player()

		self.assertEqual(self.player.level, 2)

	def test_reset_player(self):
		self.player.reset_player()

		self.assertEqual(self.player.rect.center, (800 - 725, 600 - 200))
		self.assertEqual(self.player.leveled_up, False)

	def test_reset_player_stats(self):
		self.player.level = 3
		self.player.points = 999
		self.player.life = 20
		self.player.reset_player_stats()

		self.assertEqual(self.player.level, 1)
		self.assertEqual(self.player.points, 0)
		self.assertEqual(self.player.life, 90)

	@patch('models.player.get_user_id')
	@patch('models.player.update_user_statistics')
	def test_update_db(self, mock_update_user_stats, mock_get_user_id):
		mock_get_user_id.return_value = 123
		self.player.update_db()
		mock_get_user_id.assert_called_once_with(
			'game_users_db', 'users', 'Test Player')
		mock_update_user_stats.assert_called_once_with(
			'game_users_db', 'game_statistics', self.player.points,
			self.player.life, self.player.level, mock_get_user_id.return_value)

	def tearDown(self):
		pygame.quit()
		patch.stopall()
