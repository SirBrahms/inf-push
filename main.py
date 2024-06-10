import pygame
from sys import exit
from Player_Manager import PlayerManager
pygame.init()

clock = pygame.time.Clock()

#screen setup
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Push")
#useful variables 
screen_center_X = screen_width // 2
screen_center_Y = screen_height // 2
player_manager = PlayerManager()

#logo
logo_done = False
logo = pygame.image.load("assets/logo.png")
logo_width, logo_height = logo.get_size()
logo_X = screen_center_X - logo_width // 2
logo_Y = screen_center_Y - logo_height // 2



running = True
while running:
    #event handler
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
            
    
    # display logo
    if not logo_done:
        screen.blit(logo, (logo_X, logo_Y))
        pygame.display.flip()
        pygame.time.delay(5000)
        screen.fill((0,0,0))
        logo_done = True
    
    
    
    
    pygame.display.update()
    
    #fps ceiling
    clock.tick(60)
    
#quitting
pygame.time.wait(4000)
pygame.quit()