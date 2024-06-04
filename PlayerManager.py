import random

#dice roll Funktion
dice_colours = ["Black", "Red", "Green", "Blue", "Orange", "Purple"]
def dice_roll():
    n = random.choice(dice_colours)
    print(n)


dice_roll()