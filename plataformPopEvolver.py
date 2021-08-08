from defs import *
from neuralNet import NeuralNet
from math import floor
from plataform import Plataform

class Evolver():
  def __init__(self, population, gameDisplay):
    self.population = population 
    self.gameDisplay = gameDisplay

  def evolve_population(self):
    self._order_population_by_points()

    best_ind = self._get_best_individuals()
    worst_ind = self._get_worst_individuals()
    worst_ind = self._mutate_parents(worst_ind)
    parents = best_ind + worst_ind    
    
    childs = self._breed(best_ind)

    self.population = parents + childs

    return self.population

  def _get_parents(self):
    best_ind = self._get_best_individuals()
    worst_ind = self._get_worst_individuals()
    worst_ind = self._mutate_parents(worst_ind)
    return best_ind + worst_ind

  def _order_population_by_points(self):
    self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
    a = []
    for plat in self.population:
      a.append(plat.fitness)
    print(a)

  def _get_best_individuals(self):
    last_best_ind = floor(GENERATION_SIZE * BEST_IND_SURVIVOR_RATE)
    return self.population[:last_best_ind]

  def _get_worst_individuals(self):
    last_worst_ind = floor(GENERATION_SIZE * WORST_IND_SURVIVOR_RATE)
    return self.population[-last_worst_ind:]

  def _mutate_parents(self, parents):
    for parent in parents:
      parent.brain.mutate()

    return parents

  def _breed(self, parents):
    childs = []
    total_of_childs = GENERATION_SIZE - len(parents)

    for i in range(total_of_childs):
      childs.append(
        Plataform(self.gameDisplay, NeuralNet.breed(parents)))

    return childs




