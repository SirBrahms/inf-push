from Card import *

class LimList():
    def __init__(self, lst):
        self.inner_list = lst
    
    def check_new_element(self, to_add):
        c_card_temp = ColourCard("aaa", "green", "1") # temporary card(s) to generate the type
        d_card_temp = DiceCard("aaa")
        s_card_temp = SwitchCard("aaaa")
        for e in self.inner_list:
            print(type(e), type(to_add), type(c_card_temp))
            if (type(e) == type(c_card_temp) and type(to_add) == type(c_card_temp)):
                if (e.colour == to_add.colour or e.number == to_add.number):
                    raise ValueError()
            elif (type(e) == type(d_card_temp) and type(to_add) == type(d_card_temp)):
                raise ValueError()
            elif (type(e) == type(s_card_temp) and type(to_add) == type(s_card_temp)):
                raise ValueError()
        return to_add
    
    def append(self, e):
        a = self.check_new_element(e)
        self.inner_list.append(a)
            