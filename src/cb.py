import pygame as pg

class Buffer:
	buf = []
	one_click = False
	double_click = False
	long_click = False
	long_counter = 0
	def __init__(self, buffer_size):
		self.size = buffer_size
		for i in range(buffer_size):
			self.buf.append([0])

	def update(self):
			self.buf.append([pg.mouse.get_pressed()[0], pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]])
			
			if len(self.buf) > self.size:
				b = []
				for i in range(self.size):
					x = len(self.buf)-(self.size-i)
					b.append(self.buf[x])
				self.buf = b


			first = self.buf[0]
			last = self.buf[self.size-1]

			if self.long_counter == 50:
				self.long_click = True
				self.one_click = False
				self.double_click = False

			elif first[0] and last[0]:
				self.long_counter += 1
				self.long_click = False
				self.one_click = False
				self.double_click = False

			elif first[0] and last[0] == False:
				self.long_click = False
				self.one_click = True
				self.double_click = False

			else:
				self.long_click = False
				self.one_click = False
				self.double_click = False				
			
	def click(self):
		return self.one_click

	def long(self):
		return self.long_click
