import pygame as pg
import sys

from src.frame import Frame
import src.cb as  clicking_buffer


class Window(Frame):
	def __init__(self, name, x, y, width, height):
		super(Frame, self).__init__()
		self.name = name

		self.x = 0
		self.y = 0
		self.width = width
		self.height = height

		self.background = (200, 200, 200)

		self.win = pg.display.set_mode((width, height))

		self.clicking_buffer = clicking_buffer.Buffer(10)


	def close(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit(0)



	def mainloop(self):
		while(1):
			self.close()
			self.clicking_buffer.update()
			self.draw()
			pg.display.update()
		