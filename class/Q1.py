# Question 1: Create a Python class "Rectangle" with attributes for length and width.
#  Create an object of the "Rectangle" class and calculate its area (length * width) and perimeter (2 * (length + width)).

# Explanation: In this question, you need to create a class to represent a rectangle, instantiate an object of that class, and then calculate and display the area and perimeter of the rectangle.

# Sample Input:
# Length: 5
# Width: 3

class Reactangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area_of_reactangle(self):
        return self.length* self.breadth
        
    def perimeter_of_reactangle(self):
        return (2*(self.length+self.breadth))
    

new_reactangle=Reactangle(2,3)
print(f'''length:-{new_reactangle.breadth}\nbreadth:-{new_reactangle.breadth}\nArea of reactangle:-{new_reactangle.area_of_reactangle()}\nparimeter of reactangle:-{new_reactangle.perimeter_of_reactangle()}''')