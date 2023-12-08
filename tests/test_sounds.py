import unittest
from io import StringIO
import sys
import time
import pygame
from decorators.sounds import Sounds
from utils import assets_library

sound_file = assets_library['sounds']['soundtrack']


class ExampleClassFinite:
    @Sounds(sound_file, loop=False)
    def example_method(self):
        return "Hello in Code Quest"


class ExampleClassInfinite:
    @Sounds(sound_file, loop=True)
    def example_method(self):
        return "Hello in Code Quest"


class TestSoundsDecorator(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def test_method_called_success(self):
        example_finite = ExampleClassFinite()
        hello_finite = example_finite.example_method()

        self.assertEqual(hello_finite, "Hello in Code Quest")

        example_infinite = ExampleClassInfinite()
        hello_infinite = example_infinite.example_method()

        self.assertEqual(hello_infinite, "Hello in Code Quest")

    def test_sound_finite(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        example = ExampleClassFinite()
        example.example_method()

        sys.stdout = sys.__stdout__

        self.assertEqual(
            captured_output.getvalue(),
f"Finite loop started\nFinite loop ended: {round(time.time())}\n"
        )

    def test_sound_infinite(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        example = ExampleClassInfinite()
        example.example_method()

        sys.stdout = sys.__stdout__

        self.assertEqual(
            captured_output.getvalue(),
            f"Infinite loop started\nInfinite loop ended: {round(time.time())}\n"
            )




