


class calculator():
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def sum(self):
        return (self.num1*self.num1 + self.num2*self.num2 + self.num3*self.num3)





a = calculator(2,4,3)

print(a.sum())

