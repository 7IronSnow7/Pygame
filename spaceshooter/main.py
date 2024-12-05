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
clock = pygame.tine.Clock()

# plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100


# imports
#--> import player
player_surface = pygame.image.load(join("spaceshooter", "images", "player.png")).convert_alpha()
#--> import star
star_surface = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
#---> player position
player_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
#----> player direction
player_direction = pygame.math.Vector2(20, -10)
#--> import star
star_surface = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
#--> import meteor
meteor_surface = pygame.image.load(join("spaceshooter", "images", "meteor.png")).convert_alpha()
#---> meteor position
meteor_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
#--> import laser
laser_surface = pygame.image.load(join("spaceshooter", "images", "laser.png")).convert_alpha()
#---> laser position
laser_rect = laser_surface.get_frect(bottomleft = (20, window_height - 20))



# Generate random star position
num_stars = 20
stars = [(randint(0, window_width), randint(0, window_height)) for i in range(num_stars)]

while running:
    clock.tick(10)
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
    
    # meteor
    display_surface.blit(meteor_surface, (meteor_rect))
    # laser
    display_surface.blit(laser_surface, (laser_rect))
    # player
    display_surface.blit(player_surface, (player_rect))
    
    # player movement
    player_rect.center += player_direction
    display_surface.blit(player_surface, player_rect.topleft)
        
    pygame.display.update()
    
    
pygame.quit()