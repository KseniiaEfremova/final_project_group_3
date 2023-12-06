import pygame
import time


class Sounds:
	def __init__(self, sound_file, loop):
		pygame.mixer.init(48000, 16, 1, 1024)
		self.sound_effect = pygame.mixer.Sound(sound_file)
		self.loop = loop

	def __call__(self, method):
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


