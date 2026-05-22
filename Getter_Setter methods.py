#Getter method & Setter method
#Getter method
class Exam:
    def __init__(self):
        self.__mark=90
    def revalue(self,marks):
        self.__mark+=marks
        return self.__mark
e=Exam()
print(e.revalue(8))
#Setter method
class Computer: #Setter methods example
    def __init__(self):
        self.__max_price=82987#Private
    def sell(self):
        print("Computer price:{}".format(self.__max_price))
    def set_maxprice(self,amount):#Setter
        self.__max_price=amount
c=Computer()
c.sell()
c.__max_price=100075
c.sell()
c.set_maxprice(20008676)
c.sell()
