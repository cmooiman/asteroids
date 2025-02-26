# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def display_score(screen, font, score):
    #Render score text "string, anti-aliasing, color, background (optional)"
    score_text = font.render(f"Score: {score}", True, "White")
    #Display the text at coordinates
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    
    dt = 0
    score = 0
    clock = pygame.time.Clock()
    
    # Set up display
    pygame.display.set_caption("Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Used to create a Font object, which can render text to a surface. pygame.font.Font(filename, size, bold=False, italic=False)
    font = pygame.font.Font(None, 36)

    #The pygame.sprite.Group class in Pygame is a container for Sprite objects. It is used to manage multiple sprites together, making it easier to update and draw them in your game. This class is particularly useful for handling groups of similar objects, such as a collection of enemies or a set of collectible items.
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

        display_score(screen, font, score)

        # Update the display
        pygame.display.flip()

        for asteroid in asteroids:
            if player.collision_check(asteroid) == True:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision_check(asteroid) == True:
                    if asteroid.split() == False:
                        score += 1
                    shot.kill()
        
        # Cap the frame rate to 60 frames per second
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()