# %%
import datetime
import time
# %%
class GetTime:
    """class to use datetime and time class"""
    
    def __init__(self):
        """get today time"""
        self.today = datetime.datetime.today()
        self.time = datetime.datetime.now()    
        
    def show_today(self):
        return f'Today is {self.time.ctime()}'
    
    def get_3(self):
        """little game where you have to get exactly 3 seconds"""
        self.start = time.time()
        while True:
            text = input('Press any keyboard')
            if text != None:
                self.end = time.time()
                break
        dif = self.end - self.start
        return round(dif, 2)
# %%
now = GetTime()
print(now.time)
# %%
now.get_3()
# %%

