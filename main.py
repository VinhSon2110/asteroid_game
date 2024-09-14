# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import * #constants

def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	running = True
	while running:
		for event in pygame.event.get(): #check if user has closed the window & exit the game loop
			if event.type == pygame.QUIT: # if they do.It'll make the window's close button work.
				return

		screen.fill((0,0,0)) #fill the screen with a solid "black" color
		pygame.display.flip() # Refresh the display
	
if __name__=="__main__":
	main()
