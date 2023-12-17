import unittest
from unittest.mock import patch
import pygame
from board import Board
from models.player import Player
from models.falling_items.falling_items_factory import FallingItemsFactory
from models.stats.life import Life
from utils import assets_library


class TestLife(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.test_falling_items = FallingItemsFactory(self.test_board)
        self.test_player = Player(
            100, 100, self.test_board, self.test_falling_items,
            "Test Player")
        self.life = Life(self.test_player, self.test_board)

    def test_life_initialization(self):

        self.assertEqual(self.life.board_instance, self.test_board)
        self.assertEqual(self.life.lives, self.test_player.life)
        self.assertEqual(self.life.height, 60)
        self.assertEqual(self.life.width, 60)
        self.assertEqual(self.life.y, 75)

    def test_pick_image_index(self):
        actual = self.life.pick_image_index(26)
        expected = 1
        self.assertEqual(actual, expected)

        actual = self.life.pick_image_index(25)
        expected = 2
        self.assertEqual(actual, expected)

        actual = self.life.pick_image_index(17)
        expected = 3
        self.assertEqual(actual, expected)

        actual = self.life.pick_image_index(10)
        expected = 4
        self.assertEqual(actual, expected)

        actual = self.life.pick_image_index(5)
        expected = 5
        self.assertEqual(actual, expected)

        actual = self.life.pick_image_index(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_update(self):
        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 90
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(
                pygame.image.load(assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 80
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(
                pygame.image.load(assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart3']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 70
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(
                pygame.image.load(assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart5']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 50
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(pygame.image.load(
                assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart3']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 30
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(
                pygame.image.load(assets_library['sprites']['heart']['heart1']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = -5
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(pygame.image.load(
                assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

        with patch.object(self.life.player_instance,
                          'get_lives') as mock_get_lives:
            mock_get_lives.return_value = 0
            current_images = self.life.update()
            current_images_str = [pygame.image.tostring(
                image, "RGBA") for image in current_images]
            expected_images = [pygame.transform.scale(
                pygame.image.load(assets_library['sprites']['heart']['heart6']),
                (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height)),
                pygame.transform.scale(pygame.image.load(
                    assets_library['sprites']['heart']['heart6']),
                    (self.life.width, self.life.height))]
            expected_images_str = [pygame.image.tostring(
                image, "RGBA") for image in expected_images]

            self.assertEqual(current_images_str, expected_images_str)

    def tearDown(self):
        pygame.quit()
        patch.stopall()
