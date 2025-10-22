# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    # Main game loop
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        # RENDER YOUR GAME HERE
        
        # flip() the display to put your work on screen
        pygame.display.flip()  
    
    # done! time to quit.
    pygame.quit()
            

if __name__ == "__main__":
    main()
