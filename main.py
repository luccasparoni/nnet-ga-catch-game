import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import pygame
import random
from defs import *
from plataform import Plataform
from ballCollection import BallCollection
from plataformCollection import PlataformCollection
from neuralNet import NeuralNet

def update_label(data, title, font, x, y, gameDisplay):
		label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
		gameDisplay.blit(label, (x, y))
		return y

def update_data_labels(gameDisplay, dt, game_time, num_iterations, points, font):
		y_pos = 10
		gap = 20
		x_pos = 10
		y_pos = update_label(round(1000/dt,2), 'FPS', font, x_pos, y_pos + gap, gameDisplay)
		y_pos = update_label(round(game_time/1000,2),'Game time', font, x_pos, y_pos + gap, gameDisplay)
		# y_pos = update_label(num_iterations,'Iteration', font, x_pos, y_pos + gap, gameDisplay)
		y_pos = update_label(points,'Total vivo', font, x_pos, y_pos + gap, gameDisplay)

def run_game():
	pygame.init()
	gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display .set_caption("Cath the ball")

	bgImg = pygame.image.load("./bg.jpg")
	clock = pygame.time.Clock()
	label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)
	
	running = True
	game_time= 0
	# plataform = Plataform(gameDisplay, NeuralNet());
	ballCollection = BallCollection(gameDisplay)
	plataformCollection = PlataformCollection(gameDisplay, ballCollection)

	while running:
		dt = clock.tick(30)
		game_time += dt

		gameDisplay.blit(bgImg, (0,0))

		keys = pygame.key.get_pressed();

		# if(keys[pygame.K_LEFT]):
		# 	plataform.move_left()
		# if(keys[pygame.K_RIGHT]):
		# 	plataform.move_right()

		# plataform.update(ballCollection)
		# ballCollection.update(dt)

		# points = plataform.get_points()
		plataformCollection.update(dt)
		points = len(plataformCollection.active_plataforms)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		update_data_labels(gameDisplay, dt, game_time, 1, points, label_font)
		pygame.display.update()

if __name__ == "__main__":
	run_game()

