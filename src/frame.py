import pygame as pg

from src.widget import Widget

class Frame(Widget):
	def __init__(self, frame, x, y, width, height):
		super(Frame, self).__init__(frame, x, y, width, height)

		self.frame = frame
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.elements = []

	def get_size(self):
		return (self.width, self.height)

	def set_background(self, red, green, blue):
		self.background = (red, green, blue)

	def add_widget(self, widget):
		self.frame.append(self)

	def draw(self, translation_x, translation_y):
		pg.draw.rect(self.win, self.background, (self.x + translation_x, self.y + translation_y, self.width, self.height))
		for element in self.elements:
			element.draw()