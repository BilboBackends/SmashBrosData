import matplotlib.pyplot as plt
import numpy as np

class Framedata:

    def __init__ (self, nair, fair, bair, dair, ftilt, dtilt, uptilt, fsmash, dsmash, upsmash, upb, downb, jab):
        self.nair = nair
        self.fair = fair
        self.bair = bair
        self.dair = dair
        self.ftilt = ftilt
        self.dtilt = dtilt
        self.uptilt = uptilt
        self.fsmash = fsmash
        self.dsmash = dsmash
        self.upsmash = upsmash
        self.upb = upb
        self.downb = downb
        self.jab = jab

    def make_list_values(self):
       self = vars(self)
       return [value for value in self.values()]

    def make_list_keys(self):
       self = vars(self)
       return [value for value in self.keys()]

    

    def plot(self):
        data = vars(self)
        data =  {k.title(): v for k, v in data.items()}
        moves = list(data.keys())
        frames = list(data.values())
        fig = plt.figure(figsize = (10, 5))
        # creating the bar plot
        plt.barh(moves, frames, color ='maroon')
        plt.xlabel("Frame")
        plt.ylabel("Move")
        plt.title('Character')
        plt.show()
       
               
mario = Framedata(3, 16, 6, 5, 5, 5, 5, 15, 5, 9, 3, 23, 2) 
donkeykong = Framedata(10, 18, 7, 14, 7, 6, 5, 22, 11, 14, 19, 12, 5)
donkeykong.plot()






