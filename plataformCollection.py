import pygame
from math import floor


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
		self._order_plataforms_by_points()
		parents = self._get_parents()
		parents = self._mutate_parents(parents)
		childs = self._breed(parents)

		self.plataforms = parents + childs
		self.active_plataforms = self.plataforms

	def _get_parents(self):
		best_ind = self._get_best_individuals()
		worst_ind = self._get_worst_individuals()
		return best_ind + worst_ind

	def _order_plataforms_by_points(self):
		self.plataforms = sorted(self.plataforms, key=lambda x: x.points, reverse=True)

	def _get_best_individuals(self):
		last_best_ind = floor(GENERATION_SIZE * BEST_IND_SURVIVOR_RATE)
		return self.plataforms[:last_best_ind]
		
	def _get_worst_individuals(self):
		last_worst_ind = floor(GENERATION_SIZE * WORST_IND_SURVIVOR_RATE)
		return self.plataforms[-last_worst_ind:]
		
	def _mutate_parents(self, parents):
		for parent in parents:
			parent.mutate()

		return parents

	def _breed(self, parents):
		childs = []
		total_of_childs = GENERATION_SIZE - len(parents)

		for i in range(total_of_childs):
			childs.append(NeuralNet.breed(parents))

		return childs




