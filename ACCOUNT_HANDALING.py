


class sayans_account:
    def __init__(self, title=None, balance=0):
       # a = "account_holder : "
        #b = "main balance : "
        self.title =title
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount     

    def withdrawal(self, amount):
        self.balance = self.balance - amount

    
    
    def getbalance(self):
        print("now current balance is :")
        return  self.balance



class Mysavings(sayans_account):
    print("initial account details :")
    def __init__(self, title=None, balance=0, interest_rate=0):
       # c = "interest rate : "
        super().__init__(title,balance)
        self.interest_rate =interest_rate  

    def interest_amount(self):
        print("my interest amount is...")
        return (self.balance * self.interest_rate / 100)


sayan = Mysavings('sumon',2000,5) 

print(sayan.title, sayan.balance, sayan.interest_rate, sep=" ")

sayan.deposit(int(input("enter deposit amount :")))

sayan.withdrawal(int(input("enter withdrawl amount :")))

print(sayan.getbalance())

print(sayan.interest_amount())


