# %%

from random import randint

class Dice:
    """simulating a roll die"""
        
    def __init__(self, side = 6):
        """create a new dice with 6 sides"""
        self.side = side
        
    def roll_dice(self):
        """roll the dice once"""
        return randint(1,self.side)
    
    def many_rolls(self, number):
        """roll the dice N times"""
        for roll in range(number):
            print(self.roll_dice())
# %%
dice = Dice()
dice.side
# %%
dice.roll_dice()
# %%
dice.many_rolls(5)
# %%
dice.side = 10
dice.many_rolls(9)
# %%
