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
        screen.fill((0,0,0))
        logo_done = True
    
    #set player number
    if not player_manager.pn_set:
        draw_text("Select number of Players:", text_font, (255,255,255), int(screen_center_X*0.5), 0)
        pn_button1 = Button(screen_width*0.1, screen_center_Y, 1, "assets/buttons/player_number_buttons/2_players_button.png")
        if pn_button1.draw(screen) == True:
            player_manager.set_player_number(2)
        pn_button2 = Button(screen_width*0.3, screen_center_Y, 1, "assets/buttons/player_number_buttons/3_players_button.png")
        if pn_button2.draw(screen) == True:
            player_manager.set_player_number(3)
        pn_button3 = Button(screen_width*0.5, screen_center_Y, 1, "assets/buttons/player_number_buttons/4_players_button.png")
        if pn_button3.draw(screen) == True:
            player_manager.set_player_number(4)
        pn_button4 = Button(screen_width*0.7, screen_center_Y, 1, "assets/buttons/player_number_buttons/5_players_button.png")
        if pn_button4.draw(screen) == True:
            player_manager.set_player_number(5)
        pn_button5 = Button(screen_width*0.9, screen_center_Y, 1, "assets/buttons/player_number_buttons/6_players_button.png")
        if pn_button5.draw(screen) == True:
            player_manager.set_player_number(6)
    else:
        screen.fill((0,0,0))
     
    pygame.display.update()
    
    #fps ceiling
    clock.tick(60)

#quitting
pygame.time.wait(4000)
pygame.quit()