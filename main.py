import pygame

# general setup
pygame.init()
window_width, window_height = 1263, 551
display_surface = pygame.display.set_mode((window_width, window_height))
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw game
    # fill the window with the red color
    display_surface.fill("red")
    pygame.display.flip()
    
    
    pygame.display.set_caption("My_first_pygame")
    
pygame.quit()