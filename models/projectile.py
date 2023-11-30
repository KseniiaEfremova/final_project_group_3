class Projectile:
	def __init__(self, x_start, y_start, direction_x, direction_y, color):
		self.x_start = x_start
		self.y_start = y_start
		self.direction_x = direction_x
		self.direction_y = direction_y
		self.color = color
		self.delay = 60
