# 3:  Define a function that takes a name and an age as arguments,
#  with age set to a default value of 18.
#   The function should print a message with the name and age
#        Input: greet_person("Alice")
#        Expected Output: "Hello, Alice! You are 18 years old."

def greet_person(name,age=18):
    print(f"Hello, {name} You are {age} years old.")

greet_person("rohit")