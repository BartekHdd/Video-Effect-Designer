import pygame as pg

class Frame:
	def __init__(self, x, y, width, height):
		self.x = 0
		self.y = 0
		self.width = 1500
		self.height = 1000

	def get_size(self):
		return (self.width, self.height)

	def set_background(self, red, green, blue):
		self.background = (red, green, blue)

	def draw(self):
		pg.draw.rect(self.win, self.background, (self.x, self.y, self.width, self.height))