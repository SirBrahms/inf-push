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
        self.mouse_position = None
        self.clicked = False
    
    def load_image(self):
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        
    def draw(self, surface):
        action = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.x, self.y))
        
        return action