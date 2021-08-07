import pygame
from defs import *
import numpy as np

class Plataform():
	def __init__(self, gameDisplay, brain):
		self.gameDisplay = gameDisplay;
		self.x = PLATAFORM_POSITION[0]
		self.y = PLATAFORM_POSITION[1]
		self.rect = self.draw()
		self.points = 0
		self.lost_balls = 0
		self.brain = brain
		self.fitness = 0
		self.is_alive = True

	def move_left(self):
		speed = PLATAFORM_SPEED
		if(self.x - speed < 0):
			self.x = 0
		else:
			self.x = self.x - speed

	def move_right(self):
		speed = PLATAFORM_SPEED
		if(self.x + speed > WINDOW_WIDTH - PLATAFORM[0]):
			self.x = WINDOW_WIDTH -  PLATAFORM[0]
		else:
			self.x = self.x + speed

	def draw(self):
		self.rect = pygame.draw.rect(
			self.gameDisplay, 
			PLATAFORM_COLOR, 
			pygame.Rect(self.x, self.y, PLATAFORM[0], PLATAFORM[1]))

		return self.rect

	def update(self):
		if(self.lost_game() == False):
			self.draw()

	def lost_game(self):
		return self.is_alive == False;

	def get_points(self):
		return self.points

	def get_rect(self):
		return self.rect

	def collide_with_ball(self, ball):
		return self.rect.colliderect(ball.get_rect())

	def predict(self, ballCollection):
		# TODO: ARRUMAR ESSA GABIARRA
		# if(len(ballCollection.balls) == 0):
		# 	input = np.array([self.x, self.y, WINDOW_WIDTH / 2, 0, BALL_SPEED])
		# else:
		ball = ballCollection.balls[0]
		input = np.array([self.x, self.y, ball.center_x, ball.center_y, BALL_SPEED])

		left, right = self.brain.predict(input)
		if(left > right):
			self.move_left()
		else:
			self.move_right()
		# self.update(ballCollection)






