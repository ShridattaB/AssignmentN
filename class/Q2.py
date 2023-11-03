# Question 2: Create a Python class "Car" with attributes for make, model, and year.
#  Create an object of the "Car" class and display its make, model, and year.

# Explanation: This question requires you to define a class
#  to represent a car, create an object of the class, and display the car's make, model, and year.

# Sample Input:
# Make: "Toyota"
# Model: "Camry"
# Year: 2020

# Sample Output:
# Car:
# Make: Toyota
# Model: Camr
# Year: 2020

class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    
new=car("Toyota","Camr",2020)

print(f"car:\nmake:{new.make}\nModel:{new.model}\nyear:{new.year}")
