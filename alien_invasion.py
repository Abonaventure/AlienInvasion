#!/usr/bin/env python

#-*- coding:utf-8 -*-

import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.ai_settings = Settings()
		
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.ai_settings.screen_width = self.screen.get_rect().width
		self.ai_settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		
		# Make the Play button.
		self.play_button = Button(self.ai_settings,self.screen,"Play")
		
		# Create an instance to store game statistics.
		self.stats = GameStats(self.ai_settings)
		self.sb = ScoreBoard(self.ai_settings,self.screen,self.stats)
		
		#Create a ship
		self.ship = Ship(self.ai_settings,self.screen)
		self.bullets = Group()
		self.aliens = Group()
		
		#Create alien group
		self._create_fleet = gf.create_fleet(self.ai_settings,self.screen,self.ship,self.aliens)
		
	def run_game(self):

		#start main cycle of game
		while True:
			"""Start the main loop for the game."""
			gf.check_events(self.ai_settings,self.screen,self.stats,
				self.play_button,self.ship,self.aliens,self.bullets)
			
			if self.stats.game_active:
				self.ship.update()
				gf.update_bullets(self.ai_settings,self.screen,self.stats,
					self.sb,self.ship,self.aliens,self.bullets)
				gf.update_aliens(self.ai_settings,self.stats,self.screen,
					self.ship,self.aliens,self.bullets)
			
			gf.update_screen(self.ai_settings,self.screen,self.stats,
				self.sb,self.ship,self.aliens,self.bullets,self.play_button)
		
if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
			
