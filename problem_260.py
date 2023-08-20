class demo:
    def __init__(self,price):  #default constructor
        print("Hello welcome ot the class")
        self.price=price
    def display(self):
        print('value passed the demo class of price is',self.price)
s=demo(100)
s.display()