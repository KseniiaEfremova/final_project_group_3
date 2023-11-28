import random
from board import Board


class Firework:
	def __init__(self, board_instance: Board):
		self.board_instance = board_instance
		self.colors = [(255, 0, 0), (0, 0, 255), (255, 255, 255)]
		self.x_pos = random.randint(10, self.board_instance.res[0] - 10)
		# self.y_pos = self.board_instance.res[1]
		self.y_pos = 550
		self.burst_y_pos = random.randint(50, self.board_instance.res[1] - 100)
		self.delay = random.randint(0, 300)
		self.color = random.choice(self.colors)
		self.y_speed = random.randint(6, 12)


