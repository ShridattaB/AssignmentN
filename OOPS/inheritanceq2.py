# Question: Create a Hierarchy of Vehicles
# Definition: Create a base class Vehicle with attributes make and model. Then, create two derived classes, Car and Motorcycle, that inherit from Vehicle and add specific attributes.

   
# Sample Input:
#    Enter the car make: Toyota
#    Enter the car model: Camry
#    Enter the motorcycle make: Honda
#    Enter the motorcycle model: CBR500R
   

   
# Sample Output:

     
# Car Details:
#      Make: Toyota
#      Model: Camry

#      Motorcycle Details:
#      Make: Honda
#      Model: CBR500R


class vechile():
    def __init__(self,make,model):
        self.make=make
        self.model=model


class car(vechile):
    def __init__(self, make, model):
        super().__init__(make, model)

class motarcycle(vechile):
    def __init__(self, make, model):
        super().__init__(make, model)

a=input("Enter the car make: ")
b=input("Enter the car model: ")
car1=car(a,b)

c=input("Enter the motorcycle make: ")
d=input("Enter the motorcycle model: ")
motarcycle1=motarcycle(c,d)

print(f'''make:{car1.make}
model:{car1.model}\n''')

print(f'''make:{motarcycle1.make}
model:{motarcycle1.model}''')






       
          