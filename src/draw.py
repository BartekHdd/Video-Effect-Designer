import pygame as pg
def rounding_rect(window, color, x, y, width, height, radius):
	pg.draw.rect(window, color, (x, y+radius, width, height-2*radius))
	pg.draw.rect(window, color, (x+radius, y, width-2*radius, height))
	pg.draw.circle(window, color, (x+radius, y+radius), radius)
	pg.draw.circle(window, color, (x+radius, y+height-radius), radius)
	pg.draw.circle(window, color, (x+width-radius, y+height-radius), radius)
	pg.draw.circle(window, color, (x+width-radius, y+radius), radius)
