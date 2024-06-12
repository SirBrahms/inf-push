from Card import *

class LimList():
    def __init__(self, lst):
        self.inner_list = lst
    
    def check_new_element(self, to_add):
        c_card_temp = ColourCard("aaa", "green", "1") # temporary card(s) to generate the type
        d_card_temp = DiceCard("aaa")
        s_card_temp = SwitchCard("aaaa")
        for e in self.inner_list:
            if (type(e) == c_card_temp and type(to_add) == c_card_temp):
                if (e.colour == to_add.colour or e.number == to_add.number):
                    raise ValueError()
            elif (type(e) == d_card_temp and type(to_add) == d_card_temp):
                raise ValueError()
            elif (type(e) == s_card_temp and type(to_add) == s_card_temp):
                raise ValueError()
    
    def append(self, e):
        self.inner_list.append(self.check_new_element(e))
            