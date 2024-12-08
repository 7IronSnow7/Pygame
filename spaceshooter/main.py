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
        
        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
                
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT])  - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN])  - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt 
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_sur, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            
        self.laser_timer()
        
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_frect(center = (randint(0, window_width), randint(0, window_height)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
    
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 2000
        
    def update(self, dt):
        self.rect.centery += 400 * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
# General setup
pygame.init()
window_width, window_height = 1263, 551
display_surface = pygame.display.set_mode((window_width, window_height))
# Changed the title of the window
pygame.display.set_caption("My_first_pygame")
running = True
clock = pygame.time.Clock()

# import
star_surf = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
meteor_surface = pygame.image.load(join("spaceshooter", "images", "meteor.png")).convert_alpha()
laser_sur = pygame.image.load(join("spaceshooter", "images", "laser.png")).convert_alpha()

# sprites
all_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)


# custom events _> meteor events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, window_width), randint(0, 0)
            Meteor(meteor_surface, (x, y), all_sprites)
    # update
    all_sprites.update(dt)

    # draw the game
    display_surface.fill("black")
    all_sprites.draw(display_surface)
    pygame.display.update()
    
pygame.quit()
 # 2:28:12
 # Exercise
 # Create a meteor on every meteor event
 # Destory the meteor sprite after 2 seconds
 # Complete exercise to move on