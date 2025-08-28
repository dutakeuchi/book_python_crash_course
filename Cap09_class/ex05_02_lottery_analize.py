# %%
from random import sample
# %%
class LotteryAnalize:
    """count how many times a prize drawn has to happen to win"""
    
    def __init__(self, your_number, numbers = range(1,60)):
        self.your_number = your_number
        self.numbers = numbers
        self.count = 0
        
    def prize_drawn(self):
        number = sample(self.numbers, k=1)
        return number[0]
    
    def check_winner(self):
        winners = self.prize_drawn()
        if self.your_number == winners:
            return 1
        else:
            return 2
        
    def count_prize_drawn(self):
        self.count = 0
        while True:
            if self.check_winner() == 1:
                self.count += 1
                break
            else:
                self.count += 1
        return self.count
# %%
asd = LotteryAnalize(5)
asd.prize_drawn()
# %%
asd.check_winner()
# %%
asd.count_prize_drawn()
# %%
