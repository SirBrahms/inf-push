import pygame

class Button:
    def __init__(self, x, y, scale, image_path):
        self.x = x
        self.y = y
        self.scale = scale
        self.image_path = image_path
    
    
    def load_image(self):
        self.image = pygame.image.load(self.image_path)
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))