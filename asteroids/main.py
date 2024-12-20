import pygame
from constants import *

pygame.init()

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        
        pygame.display.flip()
        
pygame.quit()
    
    
if __name__ == "__main__":
    main()
    