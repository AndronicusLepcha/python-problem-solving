
#serilzation of an object
import jsonpickle
#serilzation of an object
class football:
    def __init__(self,goat1,goat2):
        self.goat1=goat1
        self.goat2=goat2
    
    def getGoat(self):
        print("the real goat is",self.goat1)
g=football('Ronaldo','MEssi')
g.getGoat()


j_string=jsonpickle.encode(g)
print(j_string)
with open('emp.json','w') as f:
    f.write(j_string)