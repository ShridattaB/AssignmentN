# Question 4: Create a Python class "Person" with attributes for
#  name, age, and city. Create an object of the "Person" class and display its name, age, and city.

# Explanation: You need to define a class to represent a person, create an object of the class, 
# and display the person's name, age, and city.

# Sample Input:
# Name: "Alice"
# Age: 30
# City: "New York"

# Sample Output:
# Person:
# Name: Alice
# Age: 30
# City: New York


class person():
    def __init__(self,name, age,city):
        self.name=name
        self.age=age
        self.city=city

    
infomartaion=person("Alice",30,"New York")

print(f"Person:\nName:{infomartaion.name}\nAge:{infomartaion.age}\ncity{infomartaion.city}")
      