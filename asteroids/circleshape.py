import pygame
# Added this to draw the player
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Apparently this will be used later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.position = pygame.Vector2(x, y)
        self.velocitiy = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass