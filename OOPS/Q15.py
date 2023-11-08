# Question 10: Create a class PersonInfo with attributes name, age, and address. Create an object to represent a person's information and display their details.

#     Sample Input:
    
#     person_info = PersonInfo("John", 30, "123 Main St")
#     Sample Output:
    
#     Name: John
#     Age: 30
#     Address: 123 Main St
    
#     Explanation: In this question, you create a class to represent a person's information and display it.

class personalinfo():
    def __init__(self,Name,age,Address):
        self.Name=Name
        self.Age=age
        self.Address=Address

personal_info=personalinfo("John",30,"123 main st")
print(personal_info.Name,personal_info.Age,personal_info.Address)