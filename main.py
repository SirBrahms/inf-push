import pygame
from sys import exit
from Player_Manager import PlayerManager
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
player_manager = PlayerManager()



scale = 1 #do not change unless absolutely necessary

#screen setup
screen_width = 1200*scale
screen_height = 700*scale
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Push")
#useful variables 
screen_center_X = screen_width // 2
screen_center_Y = screen_height // 2

def clear():
    screen.fill((0,0,0))

def player_number_screen():
    clear()
    draw_text("Select Number of Players (2-6)", text_font, (255,255,255), 10, 0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_2:
            player_manager.set_player_number(2)
        if event.key == pygame.K_3:
            player_manager.set_player_number(3)
        if event.key == pygame.K_4:
            player_manager.set_player_number(4)
        if event.key == pygame.K_5:
            player_manager.set_player_number(5)
        if event.key == pygame.K_6:
            player_manager.set_player_number(6)

def player_mode_screen():
    clear()
    draw_text("Select Safe or Risky Game Mode (s or r)", text_font, (255,255,255), 10, 0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            player_manager.set_gamemode(False)
        if event.key == pygame.K_r:
            player_manager.set_gamemode(True)

#logo
logo_done = False
logo = pygame.image.load("assets/logo.png")
logo_width, logo_height = logo.get_size()
logo_X = screen_center_X - logo_width // 2
logo_Y = screen_center_Y - logo_height // 2

#text stuff
text_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf", screen_width//24)
def draw_text(text, font, colour, x, y):
    image = font.render(text, True, colour)
    screen.blit(image, (x,y))

running = True
while running:
    pygame.display.flip()
    #event handler
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        #set player number
        if logo_done and not player_manager.pn_set:
            player_number_screen()
        #set gamemode            
        if player_manager.pn_set and not player_manager.mode_set:
            player_mode_screen()
        
    #display logo
    if not logo_done:
        screen.blit(logo, (logo_X, logo_Y))
        pygame.display.flip()
        pygame.time.delay(5000)
        clear()
        logo_done = True
        
    #fps ceiling
    clock.tick(60)
#quitting
pygame.time.wait(4000)
pygame.quit()