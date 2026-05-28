#Encapsulation and inheritance
class BankAcc:
    def __init__(self,name,balance):
        self.name=name#Public
        self.__balance=balance#Private
    def deposit(self,amount):
        self.__balance+=amount
        print(amount,"deposited")
    def get_balance(self):
        return self.__balance
class SavingAcc(BankAcc):
    def __init__(self,name,balance,interest):
        #self.name=name
        #self.__balance=balance
        super().__init__(name,balance)
        self.__interest=interest
    def display(self):
        print("Name:",self.name)
        print("Balance:",self.get_balance())
        print("Interest:",self.__interest)
s=SavingAcc("Radhakrishna",98000,2)
s.deposit(800090)
s.display()
