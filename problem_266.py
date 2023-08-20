class football:
    def __init__(self,goat1,goat2):
        self.goat1=goat1
        self.goat2=goat2
    
    def getGoat(self):
        print("the real goat is",self.goat1)
    
    go="Messi"
    
    @classmethod
    def nextGoat(cls):
        print("GOAT is ",cls.go)

    @staticmethod
    def greatest(name):
        print("the last goat is ",name)

g=football('Ronaldo','MEssi')
g.getGoat()
g.nextGoat()
g.greatest('andro')