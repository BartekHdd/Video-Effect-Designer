import pygame as pg

class Buffer:
	buf = []
	def __init__(self, buffer_size):
		self.size = buffer_size
		for i in range(buffer_size):
			self.buf.append([])
		print(self.buf)

	def update(self):
			self.buf.append([pg.mouse.get_pressed()[0], pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]])
			if len(self.buf) > self.size:
				b = []
				for i in range(self.size):
					x = len(self.buf)-(self.size-i)
					b.append(self.buf[x])
				self.buf = b
			print(self.buf)

	def click(self):
		pass
