
# imports
import pygame
from pygame.locals import *
import time
import random
import sys

pygame.init()

# colors and fonts
BLACK = (0, 0 , 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FUCHSIA = (255, 0, 255)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
HEADER_FONT = pygame.font.SysFont('timesnewromanbold.ttf', 40) 
SMALL_FONT = pygame.font.SysFont('timesnewroman.ttf', 16)
SENTENCE = 'This is the text I will type for now'

# constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = DARK_GRAY
ACTIVE_COLOR = GREEN
INACTIVE_COLOR = OLIVE
HEADER_COLOR = GREEN
TEXT_COLOR = WHITE

class Game:

	# initialize our GUI window
	def __init__(self, width, height):

		# Create the screen
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.screen.fill(DARK_GRAY)

		# Start the clock
		self.clock = pygame.time.Clock()

		# Title box
		self.title = pygame.Rect(0, 0, 320, 60)
		self.title.center = (SCREEN_WIDTH * 0.50, SCREEN_HEIGHT * 0.20)
		self.title_text = HEADER_FONT.render('Typing Speed Test', True, HEADER_COLOR)
		self.screen.blit(self.title_text, (self.title.x + 5, self.title.y + 5))

		# User input box
		self.text_box = Input_Box(self.screen, SCREEN_WIDTH * 0.50, SCREEN_HEIGHT * 0.60, SCREEN_WIDTH * 0.50, 60)
		
		# Sentence to type box
		self.sentence = pygame.Rect(0, 0, SCREEN_WIDTH * 0.50, 30)
		self.sentence.center = (SCREEN_WIDTH * 0.50, SCREEN_HEIGHT * 0.40)
		self.sentence_text = SMALL_FONT.render(SENTENCE, True, TEXT_COLOR)
		self.screen.blit(self.sentence_text, (self.sentence.x + 5, self.sentence.y + 5))

		# Results box (time, speed, etc.)
		self.results = pygame.Rect(0, 0, SCREEN_WIDTH * 0.50, 30)
		self.results.center = (SCREEN_WIDTH * 0.50, SCREEN_HEIGHT * 0.80)
		self.results_text = 'Results will be shown here'
		self.results_surface = SMALL_FONT.render(self.results_text, True, TEXT_COLOR)
		self.screen.blit(self.results_surface, (self.results.x + 5, self.results.y + 5))

	def show_results(self):
		time = self.text_box.get_elapsed_time()

		# clear old results
		pygame.draw.rect(self.screen, BACKGROUND_COLOR, self.results)
		self.results_text = ''

		# show new resultsß
		self.results_text = 'Time was... ' + str(time)
		self.results_surface = SMALL_FONT.render(self.results_text, True, TEXT_COLOR)
		self.screen.blit(self.results_surface, (self.results.x + 5, self.results.y + 5))
	
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				self.text_box.event(event)
				if (self.text_box.is_active() == False) and (self.text_box.get_start_time() != 0):
					self.show_results()
					self.text_box.reset()

			#self.text_box.update()
			self.text_box.draw()

			pygame.display.flip()
			self.clock.tick(40)

class Input_Box:

	def __init__(self, screen, centerx, centery, w, h):
		self.screen = screen
		self.rect = pygame.Rect(0, 0, w, h)
		self.rect.center = (centerx, centery)
		self.text = ''
		self.text_surface = SMALL_FONT.render(self.text, True, TEXT_COLOR)
		self.active = False
		self.start_time = 0
		self.end_time = 0

	def is_active(self):
		return self.active

	def get_start_time(self):
		return self.start_time

	def reset(self):
		self.start_time = 0
		self.end_time = 0
		#self.text = ''

	def get_elapsed_time(self):
		if self.end_time > self.start_time:
			return self.end_time - self.start_time
		else:
			return 0

	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and self.active == False:
			pos = pygame.mouse.get_pos()
			if self.rect.collidepoint(pos):
				self.active = True
				self.text = ''
				self.text_surface = SMALL_FONT.render(self.text, True, BACKGROUND_COLOR)
			else:
				pass
		elif self.active == True:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
					self.end_time = time.time()
					self.active = False
				else:
					if self.start_time == 0:
						self.start_time = time.time()
					# To be fixed later -- delete doesnt erase characters from screen
					if event.key == pygame.K_BACKSPACE:
						self.text = self.text[:-1]
					else:
						self.text = self.text + event.unicode

	def update(self):
		# will eventually resize the rectangle if needed
		pass

	def draw(self):
		if self.active:
			pygame.draw.rect(self.screen, ACTIVE_COLOR, self.rect, 2)
			self.text_surface = SMALL_FONT.render(self.text, True, TEXT_COLOR)
			self.screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
		else:
			pygame.draw.rect(self.screen, BACKGROUND_COLOR, self.rect)
			pygame.draw.rect(self.screen, INACTIVE_COLOR, self.rect, 2)

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
game.run()
pygame.quit()
sys.exit()
