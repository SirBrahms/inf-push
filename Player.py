import main
import Card

class Player:
    def __init__(self,name,avatar, avatar_X, avatar_Y):
        self.name=name
        self.avatar=avatar
        self.avatar_X=avatar_X
        self.avatar_Y=avatar_Y
        self.score=0
        

        # card lists
        self.cards_green = []
        self.cards_red = []
        self.cards_blue = []
        self.cards_yellow = []
        self.cards_purple = []

    def get_card_and_place(self, stack_num):
        card = main.player_manager.get_card()
        main.player_manager.add_card_to_stack(card, stack_num)

    def get_card_stack(self, stack_num):
        lst_temp = main.player_manager.stacks[stack_num].inner_list
        c_card_temp = Card.Colourcard("colour", "green", "1") # temporary card to generate the type

        for e in lst_temp:
            if (type(e) == type(c_card_temp)):
                if (e.colour == "green"):
                    self.cards_green.append(e)
                elif (e.colour == "red"):
                    self.cards_red.append(e)
                elif (e.colour == "blue"):
                    self.cards_blue.append(e)
                elif (e.colour == "yellow"):
                    self.cards_yellow.append(e)
                elif (e.colour == "purple"):
                    self.cards_purple.append(e)

    def secure_color(self):
        pass