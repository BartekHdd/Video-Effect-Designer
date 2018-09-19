import sys
import src.gui as gui

class VideoEffectDesigner:
	def __init__(self):
		self.win = gui.Window("Video Effect Designer", 500, 500, 1500, 1000)
		self.win.set_background(150, 150, 150)

		self.menu = gui.Frame(self.win, 0, 0, 1500, 70)
		self.menu.set_background(60, 60, 60)
		self.win.add_widget(self.menu)

		self.b = gui.Button(self.menu, 10, 10, 50, 50)
		self.menu.add_widget(self.b)

		self.time_line = gui.Frame(self.win, 0, 670, 1500, 330)
		self.time_line.set_background(60, 60, 60)
		self.win.add_widget(self.time_line)

	def run(self):
		self.win.mainloop()