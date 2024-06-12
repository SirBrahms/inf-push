import pygame
import random
from sys import exit
from bridge import *
from Player import Player
from Card import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()
#player_manager = PlayerManager()
player_manager.generate_cards()


scale = 1 #do not change unless absolutely necessary

#screen setup
screen_width = 1200*scale #do not change!
screen_height = 700*scale #do not change!
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Push")
#useful variables 
screen_center_X = screen_width//2
screen_center_Y = screen_height//2
white = (255,255,255)
yellow = (255,255,0)
def clear():
    screen.fill((0,0,0))

def quit_handler():
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        exit()
        
def player_number_screen():
    player_number_screen = True
    player_background = pygame.image.load("assets/backgrounds/select_players_background.png")
    player_background = pygame.transform.scale(player_background, (screen_width, screen_height))
    current_selection = 0
    while player_number_screen:
        screen.blit(player_background,(0,0))
        draw_text("Select Number of Players", text_font, white, 320, 10)
        if current_selection == 0:
            draw_text("2", title_font, yellow,150,260)
            draw_text("3", title_font, white,350,260)
            draw_text("4", title_font, white,550,260)
            draw_text("5", title_font, white,750,260)
            draw_text("6", title_font, white,950,260)
            
        elif current_selection == 1:
            draw_text("2", title_font, white,150,260)
            draw_text("3", title_font, yellow,350,260)
            draw_text("4", title_font, white,550,260)
            draw_text("5", title_font, white,750,260)
            draw_text("6", title_font, white,950,260)
           
        elif current_selection == 2:
            draw_text("2", title_font, white,150,260)
            draw_text("3", title_font, white,350,260)
            draw_text("4", title_font, yellow,550,260)
            draw_text("5", title_font, white,750,260)
            draw_text("6", title_font, white,950,260)
            
        elif current_selection == 3:
            draw_text("2", title_font, white,150,260)
            draw_text("3", title_font, white,350,260)
            draw_text("4", title_font, white,550,260)
            draw_text("5", title_font, yellow,750,260)
            draw_text("6", title_font, white,950,260)
            
        elif current_selection == 4:
            draw_text("2", title_font, white,150,260)
            draw_text("3", title_font, white,350,260)
            draw_text("4", title_font, white,550,260)
            draw_text("5", title_font, white,750,260)
            draw_text("6", title_font, yellow,950,260)
            
        pygame.display.flip()
        for event in pygame.event.get():
            quit_handler()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_selection != 4:
                    current_selection += 1
                if event.key == pygame.K_LEFT and current_selection != 0:
                    current_selection -=1
                if event.key == pygame.K_RETURN:
                    player_number_screen = False
                    player_manager.set_player_number(current_selection + 2)
        pn_reg()

def player_mode_screen():
    game_mode_screen = True
    game_mode_background = pygame.image.load("assets/backgrounds/game_mode_background.png")
    game_mode_background = pygame.transform.scale(game_mode_background, (screen_width, screen_height))
    current_selection = 0
    while game_mode_screen:
        screen.blit(game_mode_background, (0,0))
        draw_text("Select Game Mode", text_font, white, 400, 10)
        if current_selection == 0:
            draw_text("safe", title_font, yellow, 150, 250)
            draw_text("risky", title_font, white, 750, 250)
        elif current_selection == 1:
            draw_text("safe", title_font, white, 150, 250)
            draw_text("risky", title_font, yellow, 750, 250)
        pygame.display.flip()
        for event in pygame.event.get():
            quit_handler()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_selection != 1:
                    current_selection += 1
                if event.key == pygame.K_LEFT and current_selection != 0:
                    current_selection -=1
                if event.key == pygame.K_RETURN:
                    game_mode_screen = False
                    if current_selection == 0:
                        player_manager.set_gamemode(False)
                    else:
                        player_manager.set_gamemode(True)


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
card_sound=pygame.mixer.Sound("assets/music/card_sound.mp3")

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
rule_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf", 40*scale)
scroll_offset = 0

def die_sides_graphic():
    die_sides=["die_black.png","die_blue.png","die_green.png","die_purple.png","die_red.png","die_yellow.png"]
    random_die_side=pygame.image.load("assets/die_sides/"+random.choice(die_sides))
    screen.blit(random_die_side,(450*scale,200*scale))
    dice_sound_effect=pygame.mixer.Sound("assets/music/dice_sound.mp3")
    pygame.mixer.Sound.play(dice_sound_effect)
    
def roll_dice():
    return_pressed=False
    while not return_pressed:
        die_sides_graphic()
        pygame.display.flip()
        pygame.time.delay(1000)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return_pressed=True
    if return_pressed:
        for i in range(3):
            die_sides_graphic()
            pygame.display.flip()
            pygame.time.delay(100)
        die_sides_graphic()
        pygame.display.flip()
        pygame.time.delay(200)
        die_sides_graphic()
        pygame.display.flip()
        pygame.time.delay(500)
        die_sides=["die_black.png","die_blue.png","die_green.png","die_purple.png","die_red.png","die_yellow.png"]
        path = "assets/die_sides/"+random.choice(die_sides)
        random_die_side=pygame.image.load(path)
        screen.blit(random_die_side,(450*scale,200*scale))
        dice_sound_effect=pygame.mixer.Sound("assets/music/dice_sound.mp3")
        pygame.mixer.Sound.play(dice_sound_effect)
        pygame.display.flip()
        pygame.time.delay(1000)
        return path

player_positions = [ 
    [screen_center_X-(screen_width//2.5), screen_center_Y-(screen_height//2.5)],
    [screen_center_X, screen_center_Y-(screen_height//2.5)],
    [screen_center_X+(screen_width//2.5), screen_center_Y-(screen_height//2.5)],
    [screen_center_X+(screen_width//2.5), screen_center_Y+(screen_height//2.5)],
    [screen_center_X, screen_center_Y+(screen_height//2.5)],
    [screen_center_X-(screen_width//2.5), screen_center_Y+(screen_height//2.5)]
    ]

player1 = Player("assets/player_icons/player_pfp_blue.png", player_positions[0][0], player_positions[0][1], screen_center_X, screen_center_Y)
player_manager.add_player(player1)
player2 = Player("assets/player_icons/player_pfp_green.png", player_positions[1][0], player_positions[1][1], screen_center_X, screen_center_Y)
player_manager.add_player(player2)
player3 = Player("assets/player_icons/player_pfp_orange.png", player_positions[2][0], player_positions[2][1], screen_center_X, screen_center_Y)
player_manager.add_player(player3)
player4 = Player("assets/player_icons/player_pfp_purple.png", player_positions[3][0], player_positions[3][1], screen_center_X, screen_center_Y)
player_manager.add_player(player4)
player5 = Player("assets/player_icons/player_pfp_red.png", player_positions[4][0], player_positions[4][1], screen_center_X, screen_center_Y)
player_manager.add_player(player5)
player6 = Player("assets/player_icons/player_pfp_yellow.png", player_positions[5][0], player_positions[5][1], screen_center_X, screen_center_Y)
player_manager.add_player(player6)

#who is playing?
def pn_reg():
    player1.is_playing = True
    player2.is_playing = True
    if player_manager.player_number >= 3:
        player3.set_is_playing(True)
    if player_manager.player_number >= 4:
        player4.set_is_playing(True)
    if player_manager.player_number >= 5:
        player5.set_is_playing(True)
    if player_manager.player_number == 6:
        player6.set_is_playing(True)

    
def table():
    player1.draw(screen)
    player2.draw(screen)
    if player3.is_playing:
        player3.draw(screen)
    if player4.is_playing:
        player4.draw(screen)
    if player5.is_playing:
        player5.draw(screen)
    if player6.is_playing:
        player6.draw(screen)
    player_manager.draw_direction(screen, screen_height, 30, screen_center_Y)
    pygame.display.flip()

def draw_players():
    for e in player_manager.players:
        if (e.is_playing):
            e.draw(screen)
    for i in range(len(player_manager.players)):
                if i == player_manager.current_player and not player_manager.stack_selection:
                    player_manager.players[i].turn = True
                else:
                    player_manager.players[i].turn = False

def stack_select():
    #print("here")
        plf = False
        player_manager.stack_selection = True
        while player_manager.stack_selection:
            draw_players()
                                
            #print (player_manager.amt_of_selecting_players, player_manager.current_player)
            if (player_manager.amt_of_selecting_players == 3):
                player_manager.current_player = player_manager.old_current_player
                player_manager.next_player()
                player_manager.amt_of_selecting_players = 0
                clear()
                pygame.display.flip()
                player_manager.stack_selection = False
                                
            for event in pygame.event.get():
                quit_handler()
                draw_players()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_1):
                        player_manager.players[player_manager.current_player].get_card_stack(0, roll_dice)
                        player_manager.amt_of_selecting_players += 1
                        player_manager.next_player(False)
                    elif (event.key == pygame.K_2):
                        player_manager.players[player_manager.current_player].get_card_stack(1, roll_dice)
                        player_manager.amt_of_selecting_players += 1
                        player_manager.next_player(False)
                    elif (event.key == pygame.K_3):
                        player_manager.players[player_manager.current_player].get_card_stack(2, roll_dice)
                        player_manager.amt_of_selecting_players += 1
                        player_manager.next_player(False)
                        pygame.display.flip()
                    


#-----------------------------------------------------------------------------------------------------------------------------------------------
if (__name__ == "__main__"):
    running = True
    setup_done = False
    plf = False
    while running:
        pygame.display.flip()
        #event handler
        for event in pygame.event.get():
        #quit event
            quit_handler()
            #set player number
            if logo_done and not player_manager.pn_set:
                player_number_screen()
            #set gamemode            
            if player_manager.pn_set and not player_manager.mode_set:
                player_mode_screen()
                if player_manager.pn_set and player_manager.mode_set:
                    clear()
        
        if not logo_done:
            screen.blit(logo, (logo_X, logo_Y))
            pygame.display.flip()
            pygame.time.delay(500) #temporarily shortened for testing
            clear()
            logo_done = True
            menu = True
            current_selection=0
            #pygame.mixer.music.play(-1) commented out because it's driving me crazy
        
        while menu:
            title_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf",150*scale)
            screen.blit(menu_background, (0, 0))
            draw_text("PUSH", title_font, (255, 255, 255), 50, 0*scale)
            draw_text("The Game", text_font, (255, 255, 255), 50,130*scale)
            if current_selection == 0:
                draw_text("Start Game", text_font, (255, 255, 0), 50, 280*scale)
                draw_text("Rules", text_font, (255, 255, 255), 50, 340*scale)
                pygame.display.flip()
            else:
                draw_text("Start Game", text_font, (255, 255, 255), 50, 280)
                draw_text("Rules", text_font, (255, 255, 0), 50, 340*scale)
                pygame.display.flip()
                
            for event in pygame.event.get():
                quit_handler()
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
                                
        if not menu:
            if logo_done and player_manager.pn_set and player_manager.mode_set and not setup_done == True:
                setup_done = True
        #----------------------------------------------------------------------------------------------
        #provisional drawing player's avatars
        if setup_done:
            clear()
            current_player:Player = player_manager.players[player_manager.current_player] # current player object
            
            ### Drawing stuff goes here
            table()
            
            while len(player_manager.cards) != 0:
                draw_players()
                card_to_stack=False
                secure_mode = False
                screen.blit(pygame.image.load("assets/cards/back_card.png"),(30,250))
                pygame.display.flip()
                
                
                for event in pygame.event.get():
                    quit_handler()
                    card_to_stack = False
                    if (event.type == pygame.KEYDOWN and not player_manager.stack_selection and not secure_mode):
                        if event.key == pygame.K_RETURN:
                            card_to_stack = True
                            current_card=player_manager.get_card()
                            screen.blit(pygame.image.load(current_card.path),(30,250))
                            pygame.mixer.Sound.play(card_sound)
                            pygame.display.flip()
                            while card_to_stack:
                                for event in pygame.event.get():
                                    quit_handler()
                                    if (event.type == pygame.KEYDOWN):
                                        draw_players()
                                        try:
                                            if (current_card == None):
                                                continue
                                            if (event.key == pygame.K_1):
                                                player_manager.add_card_to_stack(current_card, 0)
                                                screen.blit(pygame.image.load("assets/cards/back_card.png"),(30,250))
                                                screen.blit(pygame.image.load(current_card.path),(330,150+len(player_manager.stacks[0].inner_list)*20))
                                                pygame.mixer.Sound.play(card_sound)
                                                card_to_stack = False
                                            elif (event.key == pygame.K_2):
                                                player_manager.add_card_to_stack(current_card, 1)
                                                screen.blit(pygame.image.load("assets/cards/back_card.png"),(30,250))
                                                screen.blit(pygame.image.load(current_card.path),(505,150+len(player_manager.stacks[1].inner_list)*20))
                                                pygame.mixer.Sound.play(card_sound)
                                                card_to_stack = False
                                            elif (event.key == pygame.K_3):
                                                player_manager.add_card_to_stack(current_card, 2)
                                                screen.blit(pygame.image.load("assets/cards/back_card.png"),(30,250))
                                                screen.blit(pygame.image.load(current_card.path),(680,150+len(player_manager.stacks[2].inner_list)*20))
                                                pygame.mixer.Sound.play(card_sound)
                                                card_to_stack = False
                                        except:
                                            # you pushed your luck!!
                                            print("you pushed your luck")
                                            side = roll_dice()
                                            color = (side.split("die_")[1].split(".png")[0])
                                            if (color == "red"):
                                                player_manager.players[current_player].cards_red.clear()
                                            elif (color == "green"):
                                                player_manager.players[current_player].cards_green.clear()
                                            elif (color == "yellow"):
                                                player_manager.players[current_player].cards_yellow.clear()
                                            elif (color == "blue"):
                                                player_manager.players[current_player].cards_blue.clear()
                                            elif (color == "purple"):
                                                player_manager.players[current_player].cards_purple.clear()
                                            elif (color == "black" and player_manager.risky_mode):
                                                player_manager.players[current_player].cards_purple.clear()
                                                player_manager.players[current_player].cards_blue.clear()
                                                player_manager.players[current_player].cards_yellow.clear()
                                                player_manager.players[current_player].cards_green.clear()
                                                player_manager.players[current_player].cards_red.clear()
                                            stack_select()
                                            
                                
                                pygame.display.flip()
                                player_manager.old_current_player = player_manager.current_player
                        # stack selection
                        elif ((event.key == pygame.K_q and not card_to_stack and not secure_mode) or plf):
                            stack_select()
                            
                        elif (event.key == pygame.K_s and not card_to_stack and not player_manager.stack_selection):
                            # secure
                            print("here")
                            secure_mode = True
                            while secure_mode:
                                for event in pygame.event.get():
                                    quit_handler()
                                    draw_players()
                                    if (event.type == pygame.KEYDOWN):
                                        if (event.key == pygame.K_r):
                                            player_manager.players[player_manager.current_player].secure_color("red")
                                            secure_mode = False
                                        elif (event.key == pygame.K_g):
                                            player_manager.players[player_manager.current_player].secure_color("green")
                                            secure_mode = False
                                        elif (event.key == pygame.K_b):
                                            player_manager.players[player_manager.current_player].secure_color("blue")
                                            secure_mode = False
                                        elif (event.key == pygame.K_y):
                                            player_manager.players[player_manager.current_player].secure_color("yellow")
                                            secure_mode = False
                                        elif (event.key == pygame.K_p):
                                            player_manager.players[player_manager.current_player].secure_color("purple")
                                            secure_mode = False
                            player_manager.next_player()
                               
        #fps ceiling
        clock.tick(60)            
        
#quitting
pygame.time.wait(4000)
pygame.quit()