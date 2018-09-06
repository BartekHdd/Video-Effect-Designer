class Widget(object):
	def __init__(self, frame, x, y, width, height):
		super(Widget, self).__init__()

		self.frame = frame
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		#frame.add_widget(self)

	#Getters
	def get_size(self):
		return (self.width, self.height)
	def get_width(self):
		return self.width
	def get_height(self):
		return self.height

	def get_pos(self):
		return (self.x, self.y)
	def get_x(self):
		return self.x
	def get_y(self):
		return self.y

	def get_background(self):
		return self.background

	#Setters
	def set_size(self, width, height):
		self.width = width
		self.height = height
	def set_width(self, width):
		self.width = width
	def set_height(self, height):
		self.height = height

	def set_pos(self, x, y):
		self.x = x
		self.y = y
	def set_x(self, x):
		self.x = x
	def set_y(self, y):
		self.y = y

	def set_background(self, red, green, blue):
		self.background = (red, green, blue)
		