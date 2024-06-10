import pygame
from sys import exit
from Player_Manager import PlayerManager
from Button import Button
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
    
#buttons
pn_button1 = Button(screen_width*0.1, screen_center_Y, 1, "assets/buttons/player_number_buttons/2_players_button.png")
pn_button2 = Button(screen_width*0.3, screen_center_Y, 1, "assets/buttons/player_number_buttons/3_players_button.png")
pn_button3 = Button(screen_width*0.5, screen_center_Y, 1, "assets/buttons/player_number_buttons/4_players_button.png")
pn_button4 = Button(screen_width*0.7, screen_center_Y, 1, "assets/buttons/player_number_buttons/5_players_button.png")
pn_button5 = Button(screen_width*0.9, screen_center_Y, 1, "assets/buttons/player_number_buttons/6_players_button.png")
safe_button = Button(screen_width*0.25, screen_center_Y, 1, "assets/buttons/gamemode_buttons/safe_button.png")
risky_button = Button(screen_width*0.75, screen_center_Y, 1, "assets/buttons/gamemode_buttons/risky_button.png")

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
            
    
    #display logo
    if not logo_done:
        screen.blit(logo, (logo_X, logo_Y))
        pygame.display.flip()
        pygame.time.delay(5000)
        clear()
        logo_done = True
    
    #set player number
    if not player_manager.pn_set:
        clear()
        draw_text("Select Number of Players:", text_font, (255,255,255), int(screen_center_X*0.5), 0)
        if pn_button1.draw(screen):
            player_manager.set_player_number(2)
        if pn_button2.draw(screen):
            player_manager.set_player_number(3)
        if pn_button3.draw(screen):
            player_manager.set_player_number(4)
        if pn_button4.draw(screen):
            player_manager.set_player_number(5)
        if pn_button5.draw(screen):
            player_manager.set_player_number(6)
        
    
    #set gamemode
    if player_manager.pn_set and not player_manager.mode_set:
        clear()
        pygame.time.wait(500)
        draw_text("Select Game Mode:", text_font, (255,255,255), int(screen_center_X*0.7), 0)
        if safe_button.draw(screen):
            player_manager.set_gamemode(False)
        if risky_button.draw(screen):
            player_manager.set_gamemode(True)
        
    
    #fps ceiling
    clock.tick(60)
#quitting
pygame.time.wait(4000)
pygame.quit()