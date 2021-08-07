from plataformPopEvolver import Evolver
import pygame


from defs import *
from plataform import Plataform
from neuralNet import NeuralNet


class PlataformCollection():
	def __init__(self, gameDisplay, ballGenerator):
		self.gameDisplay = gameDisplay
		self.plataforms = []
		self.create_generation()
		self.ballGenerator = ballGenerator
		self.active_plataforms = []

	def create_generation(self):
		self.plataforms = []

		for i in range(GENERATION_SIZE):
			self.plataforms.append(Plataform(self.gameDisplay, NeuralNet()))

		self.active_plataforms = self.plataforms


	def update(self, dt):
		self.ballGenerator.update(dt)
		self.active_plataforms = self._get_active_plataforms()

		self._predict_movements()
		self._update_plataforms()

		self._kill_losers()

		if(self._all_died()):
			self._evolve()
			self.ballGenerator.reset()

	def _get_active_plataforms(self):
		plat = []
		for plataform in self.plataforms:
			if (plataform.lost_game() == False):
				plat.append(plataform)

		return plat

	def _predict_movements(self):
		for plataform in self.active_plataforms:
			plataform.predict(self.ballGenerator)

	def _kill_losers(self):
		ball_is_in_catch_area = self._ball_is_in_catch_area()
		if(ball_is_in_catch_area):
			self._kill_all_that_didnt_catch()

	def _all_died(self):
		return len(self.active_plataforms) == 0

	def _ball_is_in_catch_area(self):
		ball = self.ballGenerator.ball
		return ball.is_inside(PLATAFORM_POSITION[1], PLATAFORM_POSITION[1] + PLATAFORM[1])

	def _kill_all_that_didnt_catch(self):
		ball = self.ballGenerator.ball

		for plataform in self.active_plataforms:
			if(plataform.catched_the_ball(ball)):
				plataform.points +=1
			else:
				plataform.is_alive = False
						

	def _update_plataforms(self):
		for plataform in self.active_plataforms:
			plataform.update()


	def _evolve(self):
		evolver = Evolver(self.plataforms)

		self.plataforms = evolver.evolve_population()
		self.active_plataforms = self.plataforms



