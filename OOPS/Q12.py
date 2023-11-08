# Question 7: Create a class Car with attributes make, model, and year. Create an object to represent a car and display its details.

#    Sample Input:
   
#    car1 = Car("Toyota", "Camry", 2020)
   


#    Sample Output:
   
#    Car Make: Toyota
#    Car Model: Camry
#    Year: 2020
   
#    Explanation: This question involves creating a class to represent a car and displaying its details.



class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    
new=car("Toyota","Camr",2020)

print(f"car:\nmake:{new.make}\nModel:{new.model}\nyear:{new.year}")