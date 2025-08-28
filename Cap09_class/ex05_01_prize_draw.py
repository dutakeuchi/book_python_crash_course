# %%
from random import sample

class Lottery:
    """"create a prize draw"""
    
    def __init__(self, drawn = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d']):
        """get all characters possible"""
        self.drawn = drawn
        
    def prize_drawn(self):
        numbers_drawn = sample(self.drawn, k=4)
        return numbers_drawn

# %%
asd = Lottery()
asd.prize_drawn()
# %%
