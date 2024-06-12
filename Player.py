from bridge import player_manager
from Card import *
import pygame

screen_height = 700 #do not change!
screen_width = 1200 #do not change!
screen_center_Y = screen_height//2
screen_center_X = screen_width//2
white = (255,255,255)

def draw_text(surface, text, font, colour, x, y):
    image = font.render(text, True, colour)
    surface.blit(image, (x,y))
    
    
class Player:
    # constructor
    def __init__(self, avatar_path, avatar_X, avatar_Y, stackset_X, stackset_Y):
        self.avatar_path = avatar_path
        self.avatar = pygame.image.load(self.avatar_path)
        self.avatar = pygame.transform.scale(self.avatar, (screen_height*0.2, screen_height*0.2))
        self.avatar_width = self.avatar.get_width()
        self.avatar_height = self.avatar.get_height()
        self.avatar_X=avatar_X
        self.avatar_Y=avatar_Y
        self.is_playing = False
        self.turn = False
        self.highlight = pygame.image.load("assets/turn_indicator.png")

        # card stuff
        self.current_card = None
        self.current_card_disp = None # current card display object (pygame.image.load)
        
        self.cards_green = []
        self.score_green = 0
        self.cards_green_icon = pygame.image.load("assets/stacks/stack_green.png")
        
        self.cards_red = []
        self.score_red = 0
        self.cards_red_icon = pygame.image.load("assets/stacks/stack_red.png")
        
        self.cards_blue = []
        self.score_blue = 0
        self.cards_blue_icon = pygame.image.load("assets/stacks/stack_blue.png")
        
        self.cards_yellow = []
        self.score_yellow = 0
        self.cards_yellow_icon = pygame.image.load("assets/stacks/stack_yellow.png")
        
        self.cards_purple = []
        self.score_purple = 0
        self.cards_purple_icon = pygame.image.load("assets/stacks/stack_purple.png")

        self.secured_cards = []
        self.score_secured = 0
        self.cards_secured_icon = pygame.image.load("assets/stacks/stack_secured.png")
        
        # card icons
        self.cards_icon_scale = screen_height*0.06
        self.cards_green_icon = pygame.transform.scale(self.cards_green_icon, (self.cards_icon_scale, self.cards_icon_scale)) #actual scaling is temp
        self.cards_red_icon = pygame.transform.scale(self.cards_red_icon, (self.cards_icon_scale, self.cards_icon_scale))
        self.cards_blue_icon = pygame.transform.scale(self.cards_blue_icon, (self.cards_icon_scale, self.cards_icon_scale))
        self.cards_yellow_icon = pygame.transform.scale(self.cards_yellow_icon, (self.cards_icon_scale, self.cards_icon_scale))
        self.cards_purple_icon = pygame.transform.scale(self.cards_purple_icon, (self.cards_icon_scale, self.cards_icon_scale))
        self.cards_secured_icon = pygame.transform.scale(self.cards_secured_icon, (self.cards_icon_scale, self.cards_icon_scale))
        self.stack_width = self.cards_green_icon.get_width()
        self.stack_height = self.cards_green_icon.get_height() #only one stack because they are all the same size
        
        self.stackset_X = self.avatar_X
        if self.avatar_Y <= screen_height//2:
            self.stackset_Y = self.avatar_Y + self.stack_width*1.3
        else:
            self.stackset_Y = self.avatar_Y - self.stack_width*2.4
        self.score=0
        
        
    # gets the top card from the deck and places it onto the stack with the passed stack_num [DO NOT USE!!!!!!!!!!!!]
    def get_card_and_place(self, stack_num:int):
        card = player_manager.get_card()
        player_manager.add_card_to_stack(card, stack_num)
    
    # get the top card and display it on the screen
    def get_card(self):
        self.current_card = player_manager.get_card()
        self.current_card_disp = pygame.image.load(self.current_card.path)
        current_card_disp_height = self.current_card_disp.get_height()
        current_card_disp_width = self.current_card_disp.get_width()
        self.current_card_disp_X = screen_center_X-current_card_disp_width//2
        self.current_card_disp_Y = screen_center_Y-current_card_disp_height//2
        return self.current_card

    # gets an enitre stack of cards (selected by the stack num), divides the ColourCards into their respective lists and does the actions of all the special cards
    def get_card_stack(self, stack_num:int, rfunc):
        lst_temp:Card = player_manager.stacks[stack_num].inner_list
        c_card_temp = ColourCard("aaa", "green", "1") # temporary card(s) to generate the type
        d_card_temp = DiceCard("aaa")
        s_card_temp = SwitchCard("aaaa")

        for f in lst_temp:
            if (type(f) == type(d_card_temp)):
                side = rfunc()
                color = (side.split("die_")[1].split(".png")[0])
                if (color == "black"):
                    lst_temp.clear()
                    return
                clipboard = []
                for e in lst_temp:
                    if (type(e) == type(c_card_temp)):
                        if (e.colour != color):
                            clipboard.append(e)
                
                lst_temp = clipboard        

        for e in lst_temp:
            if (type(e) == type(c_card_temp)):
                if (e.colour == "green"):
                    self.cards_green.append(e)
                elif (e.colour == "red"):
                    self.cards_red.append(e)
                elif (e.colour == "blue"):
                    self.cards_blue.append(e)
                elif (e.colour == "yellow"):
                    self.cards_yellow.append(e)
                elif (e.colour == "purple"):
                    self.cards_purple.append(e)
            elif (type(e) == type(s_card_temp)):
                player_manager.switch_direction()
        
        self.count_individual_scores()
    
    # counts the score per color and updates the connected variables
    def count_individual_scores(self):
        # reset everything since old cards don't go away
        self.score_green = 0
        self.score_red = 0
        self.score_blue = 0
        self.score_yellow = 0
        self.score_purple = 0
        self.score_secured = 0
        
        # count
        for e in self.cards_green:
            self.score_green += e.number
        for e in self.cards_red:
            self.score_red += e.number
        for e in self.cards_blue:
            self.score_blue += e.number
        for e in self.cards_yellow:
            self.score_yellow += e.number
        for e in self.cards_purple:
            self.score_purple += e.number
        for e in self.secured_cards:
            self.score_secured += e.number
    
    # counts the final score by adding up the value of each card
    def count_score(self):
        self.score = self.score_green + self.score_blue + self.score_purple + self.score_red + self.score_yellow + self.score_secured

    # moves an entire color into the secured_cards list
    def secure_color(self, color:str):
        if (color == "red"):
            self.secured_cards += self.cards_red
            self.cards_red.clear()
        if (color == "green"):
            self.secured_cards += self.cards_green
            self.cards_green.clear()
        if (color == "blue"):
            self.secured_cards += self.cards_blue
            self.cards_blue.clear()
        if (color == "yellow"):
            self.secured_cards += self.cards_yellow
            self.cards_yellow.clear()
        if (color == "purple"):
            self.secured_cards += self.cards_purple
            self.cards_purple.clear()
    
    # sets whether the player is playing
    def set_is_playing(self, is_playing:bool):
        self.is_playing = is_playing
        
    #display stacks (work in progress)
    """    
    def stack_disp(self, surface):
        stack_disp_Y = screen_center_Y
        for e in player_manager.stacks:
            if e == 0:
                stack_disp_X = screen_center_x*0.75
            elif e == 1:
                stack_disp_X = screen_center_x
            elif e==2:
                stack_disp_X = screen_center*1.25
            for i in player_manager.stacks[e]:
                #draw image
                surface.blit(player_manager.stacks[e][i], (stack_disp_X, stack_disp_Y))
                #move place coords down a bit
                stack_disp_Y+=50
    """
    # draws the player to the screen (tysm Michael)    
    def draw(self, surface):
        self.stack_width = self.cards_green_icon.get_width()
        self.stack_height = self.cards_green_icon.get_height() #only one stack because they are all the same size
        
        avatar_center_X = self.avatar_X - self.avatar_width//2
        avatar_center_Y = self.avatar_Y - self.avatar_height//2
        
        cards_green_icon_X = self.stackset_X - 3*(self.stack_width//2)
        cards_green_icon_Y = self.stackset_Y - self.stack_height//2
        
        cards_red_icon_X = self.stackset_X - 3*(self.stack_width//2)
        cards_red_icon_Y = self.stackset_Y + self.stack_height//2
        
        cards_blue_icon_X = self.stackset_X - self.stack_width//2
        cards_blue_icon_Y = self.stackset_Y - self.stack_height//2
        
        cards_yellow_icon_X = self.stackset_X - self.stack_width//2
        cards_yellow_icon_Y = self.stackset_Y + self.stack_height//2
        
        cards_purple_icon_X = self.stackset_X + (self.stack_width//2)
        cards_purple_icon_Y = self.stackset_Y - self.stack_height//2
        
        cards_secured_icon_X = self.stackset_X + (self.stack_width//2)
        cards_secured_icon_Y = self.stackset_Y + self.stack_height//2
        
        text_font = pygame.font.Font("assets/fonts/Tiny5/Tiny5-Regular.ttf", (self.stack_height//4)*3)
        
        surface.blit(self.avatar, (avatar_center_X, avatar_center_Y))
        if self.turn:
            self.highlight = pygame.transform.scale(self.highlight, (self.avatar_width*1.2, self.avatar_height*1.5))
            if avatar_center_Y <= screen_height//2:
                surface.blit(self.highlight, (avatar_center_X-15, avatar_center_Y))
            else:
                surface.blit(self.highlight, (avatar_center_X-15, avatar_center_Y-75))
        surface.blit(self.cards_green_icon, (cards_green_icon_X, cards_green_icon_Y))
        draw_text(surface, str(self.score_green), text_font, white, cards_green_icon_X+8, cards_green_icon_Y+4)
        
        surface.blit(self.cards_red_icon, (cards_red_icon_X, cards_red_icon_Y))
        draw_text(surface, str(self.score_red), text_font, white, cards_red_icon_X+8, cards_red_icon_Y+4)
        
        surface.blit(self.cards_blue_icon, (cards_blue_icon_X, cards_blue_icon_Y))
        draw_text(surface, str(self.score_blue), text_font, white, cards_blue_icon_X+8, cards_blue_icon_Y+4)
        
        surface.blit(self.cards_yellow_icon, (cards_yellow_icon_X, cards_yellow_icon_Y))
        draw_text(surface, str(self.score_yellow), text_font, white, cards_yellow_icon_X+8, cards_yellow_icon_Y+4)
        
        surface.blit(self.cards_purple_icon, (cards_purple_icon_X, cards_purple_icon_Y))
        draw_text(surface, str(self.score_purple), text_font, white, cards_purple_icon_X+8, cards_purple_icon_Y+4)
        
        surface.blit(self.cards_secured_icon, (cards_secured_icon_X, cards_secured_icon_Y))
        draw_text(surface, str(self.score_secured), text_font, white, cards_secured_icon_X+8, cards_secured_icon_Y+4)
        
        if avatar_center_Y <= screen_height//2:
            draw_text(surface, "Score: "+str(self.score), text_font, white, avatar_center_X, avatar_center_Y)
        else:
            draw_text(surface, "Score: "+str(self.score), text_font, white, avatar_center_X, avatar_center_Y+100)
        