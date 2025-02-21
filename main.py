# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with a color
        screen.fill("black")
        player.draw(screen)
        
        player.update(dt)

        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate to 60 frames per second
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()