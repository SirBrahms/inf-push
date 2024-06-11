import random
 
class Card():
    def __init__(self, path):
        self.path = None
 
class ColourCard(Card):
    def __init__(self, path, colour, number):
        super().__init__(path)
        self.colour = colour
        self.number = number
 
class Switch(Card):
    def __init__(self, path):
        self.path = path
        

class Dicecard(Card):
    def __init__(self, path):
        super().__init__(path)


    


