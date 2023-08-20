#serilzation of an object
import pickle
class football:
    def __init__(self,goat1,goat2):
        self.goat1=goat1
        self.goat2=goat2
    
    def getGoat(self):
        print("the real goat is",self.goat1)
g=football('Ronaldo','MEssi')
g.getGoat()

with open('goat.ser','wb') as f:
    pickle.dump(g,f)