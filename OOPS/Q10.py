# Question 5: Create a class Person with attributes name and age. Add a method is_adult that returns True if the person is 18 or older. Create an object and check if the person is an adult.

#    Sample Input:
   
#    person1 = Person("Alice", 20)
#    is_adult = person1.is_adult()
   
#    Sample Output:
   
#    Alice is an adult: True
   
class Person():
    def __init__(self,name,Age):
        self.name=name
        self.age=Age

    def is_Adult(self):
        if self.age>18:
            return True

is_adult=Person("Alice",20)
print(f"{is_adult.name} is adult: {is_adult.is_Adult()}" )
       
