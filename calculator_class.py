

class calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def multi(self):
        return self.num1 * self.num2
    def devide(self):
        return self.num1 / self.num2

cal = calculator(4,2) 

print(cal.add())
print(cal.sub())
print(cal.multi())
print(cal.devide())

        

