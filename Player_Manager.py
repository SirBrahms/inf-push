from LimList import *


class PlayerManager:
    def __init__(self):
        self.cards = []
        self.players = []
        self.player_number = 0
        self.pn_set = False
        self.stacks = [LimList([]), LimList([]), LimList([])]
        self.direction = 1 # 1 = right / -1 = left
        self.end_game_req = False
    
    def get_card(self):
        if (len(self.cards) - 1 == 0):
            self.end_game_req = True
        return self.cards.pop()
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.pn_set = True
        
    def add_card_to_stack(self, card, stack_number):
        self.stacks[stack_number].append(card)
    
    def switch_direction(self):
        self.direction *= -1
    
