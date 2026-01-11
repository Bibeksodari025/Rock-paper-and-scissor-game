# simple bike rental system using oop in python
class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total bikes:",self.stock)
    def rentforbike(self,quantity):
        if quantity<=0:
            print("Enter the quantity which is greater the zero and positive:")
        elif quantity>self.stock:
            print("Enter the value which is less than stock:")
        else:
            self.stock=self.stock-quantity
            print("Total price:",quantity*100)
            print("Total bike:",self.stock)

while True:
    obj=bikeshop(100)
    uc=int(input('''
1. Display stock
2. Rent a bike
3. Exit       '''))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the quantity->:"))
        obj.rentforbike(n)    
    else:
        break    

    
