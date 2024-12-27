import pygame
from constants import *
from player import *
            
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    # player_velocity_x = 200
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # update player position
        # x += player_velocity_x * dt
        # player.update(x, y)
        
        # Drawing
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000
        
pygame.quit()
    
    
if __name__ == "__main__":
    main()