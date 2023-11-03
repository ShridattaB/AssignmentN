# Question 5: Define a Python class "Circle" with an attribute for the radius. Create an object of
#  the "Circle" class and calculate its area (πr²) and circumference (2πr).

# Explanation: In this question, you'll create a class to represent a circle,
#  instantiate an object of the class, and calculate and display the circle's area and circumference.

# Sample Input:
# Radius: 4

# Sample Output:
# Circle:
# Radius: 4
# Area: 50.265
# Circumference: 25.132


class circle():
    def __init__(self,radius):
        self.radius=radius
    

    def area_circle(self):
        return (3.14 * self.radius*self.radius)
    
    def circumfarance_circle(self):
        return(2*3.14*self.radius)
    

circlr_info=circle(4)

print(f"circle:\nRadius:{circlr_info.radius}\nArea:{circlr_info.area_circle()}\nCircumference:{circlr_info.circumfarance_circle()}")
