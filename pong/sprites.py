from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        # image
        self.image = pygame.Surface(SIZE['paddle'])
        self.image.fill(COLORS['paddle'])
        
        # rect & movement
        self.rect = self.image.get_frect(center = POS['player'])
        self.direction = 0
        
    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
    
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])