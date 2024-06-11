import random
 
class Card():
    def __init__(self, path):
        self.path = None
 
class ColourCard(Card):
    def __init__(self, path, colour, number):
        super().__init__(path)
        self.colour = colour
        self.number = number
 
class SwitchCard(Card):
    def __init__(self, path):
        self.path = path
        

class DiceCard(Card):
    def __init__(self, path):
        super().__init__(path)


    


