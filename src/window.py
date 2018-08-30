import pygame as pg

from src.frame import Frame


class Window(Frame):
	def __init__(self, name, x, y, width, height):
		super(Frame, self).__init__()

		self.win = pg.display.set_mode((width, height))
		