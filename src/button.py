import pygame as pg

from src.widget import Widget
import src.draw as draw

class Button(Widget):
	def __init__(self, frame, x, y, width, height, text="Button"):
		super(Button, self).__init__(frame, x, y, width, height)
		self.text = text

		self.normal = {
			"background":(180, 180, 180)
		}
		self.hover = {
			"background":(150, 150, 150)		
		}
		self.press = {
			"background":(30, 230, 80)	
		}

	def on_click(self):
		print("click")
	def on_double_click(self):
		pass
		print("double")
	def on_long_click(self):
		print("long")
		pass
	def on_hover(self):
		print("hover")


	def draw(self, window, translation_x, translation_y):
		mouse = self.frame.get_mouse()

		if mouse["x"]>self.x and mouse["x"]<self.x+self.width and mouse["y"]>self.y and mouse["y"]<self.y+self.height:
			if mouse["long_click"]:
				self.on_long_click()
				self.qualities = self.press
			elif mouse["double_click"]:
				self.on_double_click()
				self.qualities = self.press
			elif mouse["one_click"]:
				self.one_click()
				self.qualities = self.press
			elif mouse["pressing"]:
				self.qualities = self.press
			else:
				self.qualities = self.hover
		else:
			self.qualities = self.normal


		background = self.qualities["background"]

		draw.rounding_rect(window, background, self.x+translation_x, self.y+translation_y, self.width, self.height, 5)
