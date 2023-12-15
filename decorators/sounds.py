import pygame
import time


class Sounds:
	"""
    A decorator class for playing sound effects during method execution.

    Attributes:
        sound_file (str): The path to the sound file.
        loop (bool): A flag indicating whether the sound should be played in a loop.
	"""

	def __init__(self, sound_file, loop):
		"""
		Initialise a Sounds instance with the sound file and loop flag.

        Args:
            sound_file (str): The path to the sound file.
            loop (bool): A flag indicating whether the sound should be played in a loop.
		"""
		pygame.mixer.init(48000, 16, 1, 1024)
		self.sound_effect = pygame.mixer.Sound(sound_file)
		self.loop = loop

	def __call__(self, method):
		"""
		Decorates a method to play the sound effect during its execution.

        Args:
            method: The method to be decorated.

        Returns:
            Callable: The decorated method.
		"""
		def wrapper(*args, **kwargs):
			if self.loop:
				print("Infinite loop started")
				self.sound_effect.play(loops=-1)
				print(f"Infinite loop ended: {round(time.time())}")
			else:
				print("Finite loop started")
				self.sound_effect.play()
				print(f"Finite loop ended: {round(time.time())}")
			return method(*args, **kwargs)
		return wrapper
