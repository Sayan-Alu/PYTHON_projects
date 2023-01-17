

class sayans_account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
        


class savings_account(sayans_account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        super().__init__(title,balance)
        self.interest_rate = interest_rate
 
#print("type in this way..: 'a',200,4")
#print("==================================================", end="\n")

#sayan = savings_account(eval(input("type account details..."))) 


sayan = savings_account('ram',50000,5)
print(sayan.title,sayan.balance,sayan.interest_rate)




