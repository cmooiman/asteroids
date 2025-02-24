# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print(updatable, drawable)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen 
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        
        updatable.update(dt)

        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate to 60 frames per second
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()