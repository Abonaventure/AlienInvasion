import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""init spaceship and init its position"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
	# ~ def __init__(self, ai_game):
		# ~ """Initialize the ship and set its starting position."""
		# ~ self.screen = ai_game.screen
		# ~ self.settings = ai_game.settings
		# ~ self.screen_rect = ai_game.screen.get_rect()
		
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
	
		#put the ship in the center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		
		#move flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""adjust ship position according to moving"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		# Update rect object from self.x.
		self.rect.centerx = self.center
		# ~ """Update the ship's position based on movement flags."""
		# ~ # Update the ship's x value, not the rect.
		# ~ if self.moving_right and self.rect.right < self.screen_rect.right:
			# ~ self.x += self.settings.ship_speed
		# ~ if self.moving_left and self.rect.left > 0:
			# ~ self.x -= self.settings.ship_speed

		# ~ # Update rect object from self.x.
		# ~ self.rect.x = self.x
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx
		# ~ self.rect.midbottom = self.screen_rect.midbottom
		# ~ self.x = float(self.rect.x)
