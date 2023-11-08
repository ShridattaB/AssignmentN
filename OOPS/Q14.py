# Question 9: Create a class Circle with an attribute radius and a method 
# calculate_area to calculate and return the area of the circle. 
# Create an object and demonstrate area calculation.

#    Sample Input:
   
#    circle = Circle(4)  
#    Sample Output:
   
#    Area of the circle is 50.27 square units.

class circle():
    def __init__(self,radius):
        self.radius=radius

    def Area_of_circle(self):
        return self.radius*self.radius
    
Calculaton=circle(4)
print(Calculaton.Area_of_circle())