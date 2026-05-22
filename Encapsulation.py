#Encapsulation
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

#Protected
class Student:
    def __init__(self):
        self._name="Krishna"
s=Student()
print(s._name)

#Private method
class Employee:
    def __init__(self):
        self.__salary=1200000
    def show(self):
        print(self.__salary)
s=Employee()
s.show()

#Deposit in bank
class Bank:
    def __init__(self):
        self.__balance=3200000
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print(self.__balance)
b=Bank()
b.deposit(9320740)
b.show_balance()

#AC
class AC:
    def __init__(self):
        self.__temp=26
    def increase(self,degree):
        self.__temp+=degree 
    def show_temp(self):
        print(self.__temp)
t=AC()
t.increase(28)
t.show_temp()

#Phone Password
class Phone:
    def __init__(self):
        self.__Password="mahadev@123"
    def check(self,pas):
        if self.__Password==pas:
            print("Unlock")
        else:
            print("Incorrect Password")
m=Phone()
m.check("mahadev@123")
