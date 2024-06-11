import random
 
class Card():
    def __init__(self, path:str):
        self.path = path
 
class ColourCard(Card):
    def __init__(self, path:str, colour:str, number:int):
        super().__init__(path)
        self.colour = colour
        self.number = number
 
class SwitchCard(Card):
    def __init__(self, path:str):
        self.path = path
        

class DiceCard(Card):
    def __init__(self, path:str):
        super().__init__(path)


    


