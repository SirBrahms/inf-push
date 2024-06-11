from LimList import *
import pygame

class PlayerManager:
    def __init__(self):
        self.cards = []
        self.players = [] #[name, av_path, av_x, av_y]
        self.player_number = 0
        self.pn_set = False
        self.stacks = [LimList([]), LimList([]), LimList([])]
        self.direction = 1 # 1 = right / -1 = left
        self.end_game_req = False
        self.risky_mode = None
        self.mode_set = False
    
    def generate_cards(self):
        pass

    def get_card(self):
        if (len(self.cards) - 1 == 0):
            self.end_game_req = True
        return self.cards.pop()
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.pn_set = True
    
    def add_player(self, name, avatar_path, avatar_X, avatar_Y):
        self.players.append([name, avatar_path, avatar_X, avatar_Y])
        
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
