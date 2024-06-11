from bridge import player_manager
from Card import *
import pygame

class Player:
    def __init__(self, avatar_path, avatar_X, avatar_Y):
        self.avatar_path = avatar_path
        self.avatar_X=avatar_X
        self.avatar_Y=avatar_Y
        self.score=0
        self.avatar = pygame.image.load(self.avatar_path)
        self.is_playing = False

        # card lists
        self.cards_green = []
        self.cards_red = []
        self.cards_blue = []
        self.cards_yellow = []
        self.cards_purple = []

        self.secured_cards = []

    def get_card_and_place(self, stack_num):
        card = player_manager.get_card()
        player_manager.add_card_to_stack(card, stack_num)

    def get_card_stack(self, stack_num):
        from main import roll_dice
        lst_temp = player_manager.stacks[stack_num].inner_list
        c_card_temp = ColourCard("aaa", "green", "1") # temporary card(s) to generate the type
        d_card_temp = DiceCard("aaa")
        s_card_temp = SwitchCard("aaaa")

        for f in lst_temp:
            if (type(f) == type(d_card_temp)):
                side = roll_dice()
                color = (side.split("die_")[1].split(".png")[0])
                lst_temp = [lst_temp for x in lst_temp if x.path.find(color) == -1]

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
        

    def count_score(self):
        for e in self.cards_green:
            self.score += e.value
        for e in self.cards_red:
            self.score += e.value
        for e in self.cards_blue:
            self.score += e.value
        for e in self.cards_yellow:
            self.score += e.value
        for e in self.cards_purple:
            self.score += e.value
        for e in self.secured_cards:
            self.score += e.value

    def secure_color(self, color):
        if (color == "red"):
            self.secured_cards += self.cards_red
        if (color == "green"):
            self.secured_cards += self.cards_green
        if (color == "blue"):
            self.secured_cards += self.cards_blue
        if (color == "yellow"):
            self.secured_cards += self.cards_yellow
        if (color == "purple"):
            self.secured_cards += self.cards_purple
    
    def set_is_playing(self, is_playing):
        self.is_playing = is_playing
            
    def draw(self, surface, screen_height):
        image = pygame.image.load(self.avatar_path)
        image = pygame.transform.scale(image, (screen_height*0.2, screen_height*0.2))
        width = image.get_width()
        height = image.get_height()
        center_X = self.avatar_X - width//2
        center_Y = self.avatar_Y - height//2
        surface.blit(image, (center_X, center_Y))