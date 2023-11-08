# Question 1: Create a Python class Student with attributes name and age. 
# Create two objects of this class and print their details.

#    Sample Input:
   
#    student1 = Student("Alice", 20)
#    student2 = Student("Bob", 22)

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=student("Bob", 22)
print(f"sudent1: studentNAme- {student1.name} studentAge- {student1.age}")

student2=student("Alice", 20)
print(f"student2: studentName- {student2.name} StudentAge- {student2.age}")



    

        