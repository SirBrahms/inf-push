import LimList

class PlayerManager:
    def __init__(self):
        self.cards = []
        self.players = []
        self.stacks = [LimList([]), LimList([]), LimList([])]
        self.direction = 1 # 1 = right / -1 = left

    def get_card(self):
        return self.cards.pop()
    
    def add_card_to_stack(self, card, stack_number):
        self.stacks[stack_number].append(card)
    
