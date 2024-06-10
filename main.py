import pygame
from sys import exit
from Player_Manager import PlayerManager
pygame.init()
pygame.font.init()
pygame.mixer.init()

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

menu_background = pygame.image.load("assets/backgrounds/menu_background.png")
menu_background = pygame.transform.scale(menu_background, (screen_width, screen_height))

rules_background = pygame.image.load("assets/backgrounds/rules_background.png")
rules_background = pygame.transform.scale(rules_background, (screen_width, screen_height))

pygame.mixer.music.load("assets/music/main_theme.mp3")

#text stuff
text_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf", screen_width//24)
def draw_text(text, font, colour, x, y):
    image = font.render(text, True, colour)
    screen.blit(image, (x,y))
    
def load_rules(filename):
    with open(filename, 'r') as file:
        rules = file.readlines()
    return rules

rules = load_rules("assets/rules.txt")
rule_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf", 40)
scroll_offset = 0

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
        if logo_done and not player_manager.pn_set and menu==False and current_selection==0:
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
        #set gamemode            
        if player_manager.pn_set and not player_manager.mode_set:
            clear()
            draw_text("Select Safe or Risky Game Mode (s or r)", text_font, (255,255,255), 10, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player_manager.set_gamemode(False)
                if event.key == pygame.K_r:
                    player_manager.set_gamemode(True)
            if player_manager.pn_set and player_manager.mode_set:
                clear()
        
    #display logo
    if not logo_done:
        screen.blit(logo, (logo_X, logo_Y))
        pygame.display.flip()
        pygame.time.delay(5000)
        clear()
        logo_done = True
        menu = True
        current_selection=0
        pygame.mixer.music.play(-1)
        
    while menu:
        title_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf",150)
        screen.blit(menu_background, (0, 0))
        draw_text("PUSH", title_font, (255, 255, 255), 50, 0)
        draw_text("The Game", text_font, (255, 255, 255), 50,130)
        if current_selection == 0:
            draw_text("Start Game", text_font, (255, 255, 0), 50, 300)
            draw_text("Rules", text_font, (255, 255, 255), 50, 360)
            pygame.display.flip()
        else:
            draw_text("Start Game", text_font, (255, 255, 255), 50, 300)
            draw_text("Rules", text_font, (255, 255, 0), 50, 360)
            pygame.display.flip()
                

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if current_selection == 0:
                        current_selection +=1                                          
                if event.key == pygame.K_UP:
                    if current_selection == 1:
                        current_selection -= 1
                if event.key == pygame.K_RETURN:
                    menu=False
                if event.key == pygame.K_RETURN and current_selection == 1:
                    rules_menu = True
                    scroll_offset = 0
                    clear()
                    while rules_menu:
                        screen.blit(rules_background, (0, 0))
                        y = 50 - scroll_offset
                        for line in rules:
                            draw_text(line.strip(), rule_font, (255, 255, 255), 50, y)
                            y += 30

                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_DOWN:
                                    scroll_offset += 30
                                if event.key == pygame.K_UP:
                                    scroll_offset -= 30
                                    if scroll_offset < 0:
                                        scroll_offset = 0
                                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                                    rules_menu = False
                                    menu = True
        
    #fps ceiling
    clock.tick(60)
    
#quitting
pygame.time.wait(4000)
pygame.quit()