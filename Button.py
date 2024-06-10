import pygame

class Button:
    def __init__(self, x, y, scale, image_path):
        self.x = x
        self.y = y
        self.scale = scale
        self.image_path = image_path
        self.width = None
        self.height = None
        self.rect = None
        self.image = None
    
    def load_image(self):
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))