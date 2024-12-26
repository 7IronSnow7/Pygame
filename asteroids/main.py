import pygame
from constants import *
from player import *
            
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player()
   
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000
        
pygame.quit()
    
    
if __name__ == "__main__":
    main()
    
# Need to add specific features, more features will be added. Another feature will be added, I swear.