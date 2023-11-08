# Question: Create a Hierarchy of Geometric Shapes
# Definition: Create a base class Shape with a method area(). Then, create two derived classes, Rectangle and Circle, that inherit from Shape and implement the area() method.

   
# Sample Input:
#    Enter the length of the rectangle: 5
#    Enter the width of the rectangle: 3
#    Enter the radius of the circle: 4
   

   
# Sample Output:
#    Rectangle Area: 15
#    Circle Area: 50.27

# class shape():
#     def area():

class shape():
    def area(self):
        pass

class reactangle(shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        return self.length*self.breadth
    
reactangle1=reactangle()
print(reactangle1.area(5,3))
    

class circle(shape):
    def area(self,radius):
        self.radius=radius
        return 3.14 *self.radius*self.radius
    

circle1=circle()
print(circle1.area(4))



    


 




