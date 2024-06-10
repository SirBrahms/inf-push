import pygame

class Button:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
    
    
    def load_image(self, image_path):
        self.image = pygame.image.load(image_path)