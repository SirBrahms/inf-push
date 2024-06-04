class Card():
    def __init__(self, Type):
        self.Type = None
        
class Colourcard(Card):
    def __init__(self, Type, colour, number):
        super().__init__(Type)
        self.colour = colour
        self.number = number
        
