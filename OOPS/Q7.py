# Question 2: Create a Python class Rectangle with attributes length and width. 
# Add a method calculate_area that calculates and returns the area of the rectangle. 
# Create an object of the class and demonstrate the area calculation.

#    Sample Input:
   
#    rectangle = Rectangle(5, 3)

#    Sample Output:
   
#    Area of the rectangle is 15 square units.

class Reactangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def Caluclate_area_reactangle(self):
        output= self.length*self.breadth
        return output
    

reactangle=Reactangle(5, 3)

print(f"Area of the rectangle is {reactangle.Caluclate_area_reactangle()} square units.")