class Widget(object):
	def __init__(self, frame, x, y, width, height):
		super(Widget, self).__init__()

		self.frame = frame
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def get_size():
		return (self.width, self.height)
	def get_width():
		return self.width
	def get_height():
		return self.height

	def get_pos():
		return (self.x, self.y)
	def get_x():
		return self.x
	def get_y():
		return self.y

	def set_size(width, height):
		self.width = width
		self.height = height
	def set_width():
		self.width = width
	def set_height():
		self.height = height

	def set_pos(x, y):
		self.x = x
		self.y = y
	def set_x(x):
		self.x
	def set_y():
		self.y
		