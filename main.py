import pygame

# General setup
pygame.init()
window_width, window_height = 1263, 551
display_surface = pygame.display.set_mode((window_width, window_height))
# Changed the title of the window
pygame.display.set_caption("My_first_pygame")
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100

# importing an image

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw game
    # fill the window with the red color
    display_surface.fill("darkgray")
    x += 0.1
    display_surface.blit(surf, (x, 150))
    pygame.display.update()
    
    
    
pygame.quit()