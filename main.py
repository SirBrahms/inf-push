import pygame
from sys import exit
from Player_Manager import PlayerManager
pygame.init()

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
logo_display_time = 5000 #milliseconds
logo_timer = pygame.time.get_ticks() 



running = True
while running:
    #event handler
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
            
    #clear screen if logo displayed for long enough
    current_time = pygame.time.get_ticks()
    if current_time - logo_timer >= logo_display_time:
        screen.fill((0, 0, 0))  
        pygame.display.flip()   
        pygame.time.delay(1000) 
        running = False
    
    #or display logo
    else:
        screen.blit(logo, (logo_X, logo_Y))
        pygame.display.flip()
    
    
    
    
    
    pygame.display.update()
    
#quitting
pygame.time.wait(4000)
pygame.quit()