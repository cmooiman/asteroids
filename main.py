# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updatable)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        # Fill the screen 
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen) 

        # Update the display
        pygame.display.flip()

        for asteroid in asteroids:
            if player.collision_check(asteroid) == True:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    asteroid.kill()
                    shot.kill()

        
        # Cap the frame rate to 60 frames per second
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()