from defs import *
import pygame
import random

class Ball():
	def __init__(self, gameDisplay):
		self.gameDisplay = gameDisplay;
		self.center_x = self.generateRandomX();
		self.center_y = 0 - BALL_DIAMETER
		self.active = True;
		self.rect = self.draw()

	def get_bottom_height(self):
		return self.center_y + BALL_DIAMETER

	def draw(self):
		self.rect = pygame.draw.circle(
			self.gameDisplay, 
			BALL_COLOR, 
			(self.center_x, self.center_y), BALL_DIAMETER * 2)
		return self.rect

	def get_rect(self):
		return self.rect

	def update(self, dt):
		self.center_y = self.center_y + BALL_SPEED * dt
		if(self.center_y > WINDOW_HEIGHT):
			self.active = False
		if(self.active == True):
			self.draw()

	def generateRandomX(self):
		return random.randint(5, WINDOW_WIDTH - 5)

	def is_active(self):
		return self.active

	def catched(self):
		self.active = False

	def is_inside(self, y1, y2):
		ball_top = self.center_y - BALL_DIAMETER
		ball_bottom = self.center_y + BALL_DIAMETER
		if(y1 < ball_top < y2 or y1 < ball_bottom < y2):
			return True
		return False

