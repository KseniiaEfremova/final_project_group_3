import pygame

class Sounds():
	def __init__(self, sound_file):
		pygame.mixer.init()
		self.sound_effect = pygame.mixer.Sound(sound_file)

	def call(self, method):
		def wrapper(*args, **kwargs):
			self.sound_effect.play()
			return method(*args, **kwargs)
		return wrapper


