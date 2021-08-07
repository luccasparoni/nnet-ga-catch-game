import pygame
from defs import *
from plataform import Plataform
from neuralNet import NeuralNet


class PlataformCollection():
	def __init__(self, gameDisplay, ballCollection):
		self.gameDisplay = gameDisplay
		self.plataforms = []
		self.create_generation()
		self.ballCollection = ballCollection
		self.active_plataforms = []

	def create_generation(self):
		self.plataforms = []

		for i in range(GENERATION_SIZE):
			self.plataforms.append(Plataform(self.gameDisplay, NeuralNet()))

		self.active_plataforms = self.plataforms


	def update(self, dt):
		self.ballCollection.update(dt)
		self.active_plataforms = self.get_active_plataforms()

		self.predict_movements()

		self.kill_losers()

		self.update_plataforms()


		if(self.all_died()):
			self.create_generation()
			self.ballCollection.reset()

	def get_active_plataforms(self):
		plat = []
		for plataform in self.plataforms:
			if (plataform.lost_game() == False):
				plat.append(plataform)

		return plat

	def predict_movements(self):
		for plataform in self.active_plataforms:
			plataform.predict(self.ballCollection)

	def kill_losers(self):
		possible_ball_colisions = self.possible_colisions_balls()
		if(len(possible_ball_colisions) > 0):
			self.kill_all_that_didnt_collide(possible_ball_colisions)

	def all_died(self):
		return len(self.active_plataforms) == 0

	def possible_colisions_balls(self):
		possible_ball_colisions = []
		for ball in self.ballCollection.balls:
			if(ball.is_inside(PLATAFORM_POSITION[1], PLATAFORM_POSITION[1] + PLATAFORM[1])):
				possible_ball_colisions.append(ball)
		return possible_ball_colisions

	def kill_all_that_didnt_collide(self, possible_ball_colisions):
		for ball in possible_ball_colisions:
			for plataform in self.active_plataforms:
				if(plataform.collide_with_ball(ball)):
					plataform.points +=1
				else:
					plataform.is_alive = False
						

	def update_plataforms(self):
		for plataform in self.active_plataforms:
			plataform.update()

