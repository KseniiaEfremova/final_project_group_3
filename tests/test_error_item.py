import unittest
import pygame
import numpy as np
from board import Board
from falling_items.damage_falling_item import ErrorItem

error_image = pygame.image.load("assets/error.gif")


class TestErrorItem(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.board = pygame.display.set_mode(
            (800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)

    def test_error_item_init(self):
        error_item = ErrorItem(error_image, self.test_board)

        self.assertEqual(error_item.width, 30)
        self.assertEqual(error_item.height, 30)
        self.assertEqual(error_item.y, 0)
        self.assertEqual(error_item.speed, 8)
        self.assertEqual(error_item.points, 5)
        self.assertEqual(error_item.damage, 10)

    def test_error_item_draw(self):
        error_item = ErrorItem(error_image, self.test_board)
        error_item.draw(self.test_board)
        error = pygame.surfarray.array3d(error_item.image)
        loaded_error = pygame.transform.scale(error_image, (30, 30))
        error_content = pygame.surfarray.array3d(loaded_error)
        diff = np.abs(error_content - error)
        total_diff = np.sum(diff)
        allowable_diff = 0

        self.assertLessEqual(total_diff, allowable_diff)

    def test_error_item_spawn(self):
        error_item = ErrorItem(error_image, self.test_board)

        self.assertFalse(error_item.x < 0)
        self.assertFalse(error_item.x == 0)
        self.assertFalse(error_item.x > 770)
        self.assertTrue(0 < error_item.x < 770)

    def test_error_item_fall(self):
        error_item = ErrorItem(error_image, self.test_board)
        error_item.draw(self.test_board)
        error_item.fall()

        self.assertTrue(error_item.y > 0)
        self.assertTrue(error_item.y >= error_item.speed)
