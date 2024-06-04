import LimList
import main

class PlayerManager:
    def __init__(self):
        self.cards = []
        self.players = []
        self.stacks = [LimList([]), LimList([]), LimList([])]
        self.direction = 1 # 1 = right / -1 = left
        self.end_game_req = False

    def get_card(self):
        if (len(self.cards) - 1 == 0):
            self.end_game_req = True
        return self.cards.pop()
    
    def add_card_to_stack(self, card, stack_number):
        self.stacks[stack_number].append(card)
    
