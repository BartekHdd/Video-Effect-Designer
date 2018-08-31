import sys
import src.gui as gui

class VideoEffectDesigner:
	def __init__(self):
		self.win = gui.Window("Video Effect Designer", 500, 500, 1500, 1000)

	def run(self):
		self.win.mainloop()