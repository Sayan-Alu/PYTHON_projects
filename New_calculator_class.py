




class calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def all_in_one(self):
       yield f" The sum of {self.num1} and {self.num2} is {self.num1 + self.num2}"
   
       yield f" The sub of {self.num1} and {self.num2} is {self.num1 - self.num2}"
    
       yield f" The Multipication of {self.num1} and {self.num2} is {self.num1 * self.num2}"
   
       yield f" The Division of {self.num1} and {self.num2} is {self.num1 / self.num2}"
   
cal = calculator(94,10)

for result in cal.all_in_one():
    print(result)

    # Expected Output:
          
           #  The sum of 94 and 10 is 104
           #  The sub of 94 and 10 is 84
           #  The Multipication of 94 and 10 is 940
           #  The Division of 94 and 10 is 9.4