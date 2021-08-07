import pygame
from defs import *
from ball import Ball

class BallCollection():
	def __init__(self, gameDisplay):
		self.gameDisplay = gameDisplay
		self.balls = []
		self.next_ball = BALL_GENERATOR_TIME_SPAN
		self.create_ball()

	def get_balls(self):
		return self.balls

	def create_ball(self):
		ball = Ball(self.gameDisplay)
		self.balls.append(ball);

	def update(self, dt):
		self.update_balls(dt)

		# self.next_ball -= 1
		# if(self.should_generate_ball()):
		# 	self.next_ball = BALL_GENERATOR_TIME_SPAN
		# 	self.create_ball()

	def update_balls(self, dt):
		for i, ball in enumerate(self.balls):
			ball.update(dt)
			if(ball.is_active() == False):
				self.balls.pop(i)
				self.create_ball()
	
	def should_generate_ball(self):
		return self.next_ball == 0

	def reset(self):
		self.balls = []
		self.next_ball = BALL_GENERATOR_TIME_SPAN
		self.create_ball()