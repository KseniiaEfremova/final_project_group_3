import unittest
from unittest.mock import MagicMock, patch
import pygame
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.stats.level import Level
from utils import assets_library


class TestLevel(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.test_falling_items = FallingItemsFactory(self.test_board)
        self.test_player = Player(100, 100, self.test_board, self.test_falling_items)
        self.level = Level(self.test_player, self.test_board)

    def test_level_initialization(self):

        self.assertEqual(self.level.board_instance, self.test_board)
        self.assertEqual(self.level.width, 70)
        self.assertEqual(self.level.height, 70)
        self.assertEqual(self.level.x, 550)
        self.assertEqual(self.level.y, 75)
        self.assertEqual(self.level.level, self.test_player.level)
        self.assertEqual(self.level.current_sprite, self.test_player.level - 1)

    def test_update(self):
        self.test_player.level = 1
        current_sprite = self.level.update()

        self.assertEqual(current_sprite, 0)

        self.test_player.level = 2
        current_sprite = self.level.update()
        self.assertEqual(current_sprite, 1)

        self.test_player.level = 3
        current_sprite = self.level.update()
        self.assertEqual(current_sprite, 2)

        self.test_player.level = 4
        current_sprite = self.level.update()
        self.assertEqual(current_sprite, 2)

    def test_draw(self):
        self.test_player.level = 1
        current_sprite = self.level.update()
        current_image = self.level.sprites[current_sprite]
        expected_image = pygame.image.load(assets_library['sprites']['level']['level1'])

        current_image_str = pygame.image.tostring(current_image, "RGBA")
        expected_image_str = pygame.image.tostring(expected_image, "RGBA")

        self.assertEqual(current_image_str, expected_image_str)

        self.test_player.level = 2
        current_sprite = self.level.update()
        current_image = self.level.sprites[current_sprite]
        expected_image = pygame.image.load(assets_library['sprites']['level']['level2'])

        current_image_str = pygame.image.tostring(current_image, "RGBA")
        expected_image_str = pygame.image.tostring(expected_image, "RGBA")

        self.assertEqual(current_image_str, expected_image_str)

        self.test_player.level = 3
        current_sprite = self.level.update()
        current_image = self.level.sprites[current_sprite]
        expected_image = pygame.image.load(assets_library['sprites']['level']['level3'])

        current_image_str = pygame.image.tostring(current_image, "RGBA")
        expected_image_str = pygame.image.tostring(expected_image, "RGBA")

        self.assertEqual(current_image_str, expected_image_str)

        self.test_player.level = 4
        current_sprite = self.level.update()
        current_image = self.level.sprites[current_sprite]
        expected_image = pygame.image.load(assets_library['sprites']['level']['level3'])

        current_image_str = pygame.image.tostring(current_image, "RGBA")
        expected_image_str = pygame.image.tostring(expected_image, "RGBA")

        self.assertEqual(current_image_str, expected_image_str)


    def test_level_up_image(self):
        pass

    def tearDown(self):
        pygame.quit()
        pygame.font.quit()
        patch.stopall()