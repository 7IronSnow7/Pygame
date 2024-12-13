import pygame
from os.path import join
from random import randint, uniform

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

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True


    def update(self, dt):
        #______________Uncomment from here to use the Keyboard movement_______________
        # keys = pygame.key.get_pressed()
        # self.direction.x = int(keys[pygame.K_RIGHT])  - int(keys[pygame.K_LEFT])
        # self.direction.y = int(keys[pygame.K_DOWN])  - int(keys[pygame.K_UP])
        # self.direction.x, self.direction.y = pygame.mouse.get_pos()
        #____________________________________________________________________________
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos
        pygame.mouse.set_visible(False)
        self.direction = pygame.Vector2(mouse_pos) - pygame.Vector2(self.rect.center)
        if self.direction.length() != 0:
            self. direction = self.direction.normalize()
            
        #______________Uncomment from here to use the Keyboard movement_______________
        # self.direction = self.direction.normalize() if self.direction else self.direction
        #____________________________________________________________________________
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        # if recent_keys[pygame.K_SPACE] and self.can_shoot: = Keyboard space button shoot
        if mouse_buttons[0] and self.can_shoot:
            Laser(laser_sur, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

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
        self.original_surf = surf
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(40, 80)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.recr = self.image.get_frect(center = self.rect.center)

class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

def collisions():
    global running

    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)
            explosion_sound.play()

def display_score():
    current_time = pygame.time.get_ticks()
    text_surf = font.render(str(current_time), True, (240, 240, 240))
    text_rect = text_surf.get_frect(midbottom =  (window_width / 2, window_height - 50))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), text_rect.inflate(20, 10).move(0, -8), 5, 10)

# General setup
pygame.init()
window_width, window_height = 1600, 1000
display_surface = pygame.display.set_mode((window_width, window_height))
# Changed the title of the window
pygame.display.set_caption("My_first_pygame")
running = True
clock = pygame.time.Clock()

# import
star_surf = pygame.image.load(join("spaceshooter", "images", "star.png")).convert_alpha()
meteor_surface = pygame.image.load(join("spaceshooter", "images", "meteor.png")).convert_alpha()
laser_sur = pygame.image.load(join("spaceshooter", "images", "laser.png")).convert_alpha()
font = pygame.font.Font(join("spaceshooter", "images", "Oxanium-Bold.ttf"), 40)
explosion_frames = [pygame.image.load(join("spaceshooter", "images", "explosion", f"{i}.png")).convert_alpha() for i in range(21)]
# text_surf = font.render("text", True, (240, 240, 240))

laser_sound = pygame.mixer.Sound(join("spaceshooter", "audio", "laser.wav"))
laser_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound(join("spaceshooter", "audio", "explosion.wav"))
# damage_sound = pygame.mixer.Sound(join("spaceshooter", "audio", "damage.ogg"))
game_music = pygame.mixer.Sound(join("spaceshooter", "audio", "game_music.wav"))
game_music.set_volume(0.2)
game_music.play(loops = -1)

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)


# custom events _> meteor events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

test_rect = pygame.FRect(0, 0, 300, 600)

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, window_width), randint(0, 0)
            Meteor(meteor_surface, (x, y), (all_sprites, meteor_sprites))
    # update
    all_sprites.update(dt)
    collisions()

    # draw the game
    display_surface.fill("black")
    all_sprites.draw(display_surface)
    display_score()

    # draw test

    pygame.display.update()

pygame.quit()
# I am creating a comment here to commit to see if this affects my boot.dev daily streak