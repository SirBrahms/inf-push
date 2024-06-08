class Card():
    def __init__(self, path):
        self.path = None
        
class Colourcard(Card):
    def __init__(self, path, colour, number):
        super().__init__(path)
        self.colour = colour
        self.number = number
        
