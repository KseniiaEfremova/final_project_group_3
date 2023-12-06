import unittest
import pygame
from unittest.mock import patch, MagicMock
from board import Board
from models.components.input_box import InputBox

pygame.mouse.get_pos = MagicMock(return_value=(0, 0))


class TestInputBox(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode((800, 600))
        self.test_board = Board("Test Board", (800, 600), 60)
        self.input = InputBox(0, 0, 100, 50, "Test Input", self.test_board)
        self.mock_surface = pygame.surface.Surface((100, 100))
    def test_input_initialization(self):

        self.assertEqual(self.input.rect, (0, 0, 100, 50))
        self.assertEqual(self.input.text, "Test Input")
        self.assertEqual(self.input.active, False)
        self.assertEqual(self.input.color, pygame.Color('gray15'))
        self.assertEqual(self.input.board_instance, self.test_board)

    def test_handle_event_mouse(self):

        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event.pos = (70, 30)

        self.input.handle_event(mock_event)

        self.assertTrue(self.input.active)

    def test_handle_event_keyboard(self):

        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.unicode = 'a'

        self.input.active = True
        self.input.handle_event(mock_event)

        self.assertEqual(self.input.text, "Test Inputa")

    def test_draw_box(self):
        f = pygame.font.Font(None, 40)
        f.render.return_value = pygame.surface.Surface((200, 200))
        self.input.draw_box()

        self.input.active = True
        self.assertTrue(self.input.text, "Test Input")
        self.assertTrue(self.input.color, pygame.Color('chartreuse3'))

        self.input.active = False
        self.assertTrue(self.input.text, "Test Input")
        self.assertTrue(self.input.color, pygame.Color('gray15'))

    def test_get_user_text(self):
        self.assertEqual(self.input.text, "Test Input")

    def tearDown(self):
        pygame.quit()
        patch.stopall()
