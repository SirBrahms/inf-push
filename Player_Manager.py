from LimList import *
from bridge2 import deck
from Card import *
import pygame
import random
import re

class PlayerManager:
    def __init__(self):
        self.cards = []
        self.generate_cards()
        self.players = []
        self.player_number = 0
        self.current_player = 0
        self.pn_set = False
        self.stacks = [LimList([]), LimList([]), LimList([])]
        self.direction = 1 # 1 = right / -1 = left
        self.end_game_req = False
        self.risky_mode = None
        self.mode_set = False
        
        self.stack_selection = False
        self.amt_of_selecting_players = 0
        self.old_current_player = 0
    
    def generate_cards(self):
        temp_list = deck[:-2]
        for e in temp_list:
            num = int(re.findall(r"[\d].*(?=\.png)", e)[0]) #regex, do not touch
            temporary_color_variable_because_python_is_fucking_stupid = re.sub(r"(?:.*\/(?:.*)\/)", "", e)
            color = re.search(r".*(?=\d\.png)", temporary_color_variable_because_python_is_fucking_stupid)[0]
            
            for i in range(3):
                self.cards.append(ColourCard(e, color, num))
        
        for i in range(18):
            self.cards.append(DiceCard(deck[len(deck) - 1]))
        
        for i in range(12):
            self.cards.append(SwitchCard(deck[len(deck) - 2]))
        
        random.shuffle(self.cards)
        
    def next_player(self):
        next = self.current_player + (1 * self.direction)
        if (next == self.player_number):
            next = 0
        elif (next < 0):
            next = self.player_number - 1
            
        self.current_player = next
    
    def get_card(self):
        if (len(self.cards) - 1 == 0):
            self.end_game_req = True
        return self.cards.pop()
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.pn_set = True
    
    def add_player(self, player):
        self.players.append(player)
        
    def set_gamemode(self, risky): #risky is a boolean
        self.risky_mode = risky
        self.mode_set = True
        
    def add_card_to_stack(self, card, stack_number):
        self.stacks[stack_number].append(card)
    
    def switch_direction(self):
        self.direction *= -1
        
    def draw_direction(self, surface, screen_height, x, y):
        if self.direction == 1:
            image = pygame.image.load("assets/arrows/counterclockwise_arrow.png")
        else:
            image = pygame.image.load("assets/arrows/clockwise_arrow.png")
        image = pygame.transform.scale(image, (screen_height*0.1, screen_height*0.1))
        width = image.get_width()
        height = image.get_height()
        center_X = x - width//2
        center_Y = y - height//2
        surface.blit(image, (center_X, center_Y))
    
    def clear_arrow_area(self, surface, x, y, screen_height):
        arrow_size = int(screen_height * 0.1)
        rect = pygame.Rect(x - arrow_size // 2, y - arrow_size // 2, arrow_size, arrow_size)
        surface.fill((0, 0, 0), rect)
