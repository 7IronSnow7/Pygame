import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("spaceshooter", "images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (window_width / 2, window_height / 2))
        self.direction = pygame.Vector2()
        self.speed = 300
        
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT])  - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN])  - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt 
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print("Fire laser")

class Star(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (randint(0, window_width), randint(0, window_height)))
        
# General setup
pygame.init()
window_width, window_height = 1263, 551
display_surface = pygame.display.set_mode((window_width, window_height))
# Changed the title of the window
pygame.display.set_caption("My_first_pygame")
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
for i in range(20):
    Star(all_sprites)
# imports
#--> import player
# player_surface = 
#--> import star
star_surface = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
#---> player position
# player_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
# player_speed = 300
#--> import star
# star_surface = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
#--> import meteor
meteor_surface = pygame.image.load(join("spaceshooter", "images", "meteor.png")).convert_alpha()
#---> meteor position
# meteor_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
#--> import laser
laser_surface = pygame.image.load(join("spaceshooter", "images", "laser.png")).convert_alpha()
#---> laser position
laser_rect = laser_surface.get_frect(bottomleft = (20, window_height - 20))



# Generate random star position
# num_stars = 20
# stars = [(randint(0, window_width), randint(0, window_height)) for i in range(num_stars)]

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # draw game
    display_surface.fill("black")
    all_sprites.draw(display_surface)
    
    pygame.display.update()
    
pygame.quit()