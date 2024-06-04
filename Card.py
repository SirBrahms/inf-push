import random
#Oberklasse fur alle Karten
class Card():
    def __init__(self, Type):
        self.Type = None
#Spielkarte mit Farbe und Zahl 
class Colourcard(Card):
    def __init__(self, Type, colour, number):
        super().__init__(Type)
        self.Type = colourcard
        self.colour = colour
        self.number = number
# Switchkarte nicht fertig
class Switch(Card):
    def __init__(self, Type):
        self.Type = switchcard
    #Variable in Playermanager mit True oder False
        
#Dice card with it's type and which colour is being deleted from the dice roll
class Dicecard(Card):
    def __init__(self, Type):
        super().__init__(Type)
        self.type = None
        self.colour_delete = None
    #dice roll
    def dice_roll(self):
        pass

    


