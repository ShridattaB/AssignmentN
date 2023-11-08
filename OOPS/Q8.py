# Question 3: Create a class Calculator with methods add, subtract, multiply, 
# and divide. Create an object and perform basic arithmetic operations using these methods.

#    Sample Input:
   
#    calc = Calculator()
#    result1 = calc.add(10, 5)
#    result2 = calc.multiply(4, 3)
   
#    Sample Output:
   
#    Addition: 10 + 5 = 15
#    Multiplication: 4 * 3 = 12


class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2
    
    def Substract(self):
        return self.num1-self.num2
    
    def multiplication(self):
        return self.num1*self.num2
    
result1=calculator(10,5)
print(result1.add())

result2=calculator(4,3)
print(result2.multiplication())


