import pygame
from os.path import join
from random import randint

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
player_surface = pygame.image.load(join("spaceshooter", "images", "player.png")).convert_alpha()
star_surface = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
player_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))

# Generate random star position
num_stars = 20
stars = [(randint(0, window_width), randint(0, window_height)) for i in range(num_stars)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw game
    # fill the window with color
    display_surface.fill("black")
    
    # Draw the stars
    for star_position in stars:
        display_surface.blit(star_surface, star_position)
    
    # player
    display_surface.blit(player_surface, (player_rect))

    pygame.display.update()
    
    
    
pygame.quit()