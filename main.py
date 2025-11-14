# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    dt = 0  # delta time between frames in seconds
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    # add groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    
    # set containers for sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot_group, updatable, drawable)
    
    # create player
    player_ship = Player(x, y)
    asteroid_field = AsteroidField()
    
    while running:
        # call logger
        log_state()
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        # RENDER YOUR GAME HERE
        updatable.update(dt)
        for asteroid in asteroids:
            if player_ship.collide(asteroid):
                print("Game over!")
                running = False
            for bullet in shot_group:
                if bullet.collide(asteroid):
                    asteroid.split()
                    bullet.kill()
                
        for sprite in drawable:
            sprite.draw(screen) 
        
        # flip() the display to put your work on screen
        pygame.display.flip()  
        
        dt = clock.tick(60) / 1000  # limits FPS to 60 and convert to seconds
    
    # done! time to quit.
    pygame.quit()
            

if __name__ == "__main__":
    main()
