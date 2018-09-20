import pygame as pg
import sys

from src.frame import Frame
import src.cb as  clicking_buffer


class Window(Frame):
	def __init__(self, name, x, y, width, height):
		super(Window, self).__init__(self, 0, 0, width, height)
		self.name = name

		self.win_x = x
		self.win_y = y
		self.background = (200, 200, 200)

		self.win = pg.display.set_mode((width, height))
		pg.display.set_caption(name)

		self.clicking_buffer = clicking_buffer.Buffer(10)


	def close(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit(0)

	def get_mouse(self):
		return self.clicking_buffer.state()

	def mainloop(self):
		while(1):
			self.close()
			self.clicking_buffer.update()
			self.draw(self.win, 0, 0)

			pg.display.update()
		