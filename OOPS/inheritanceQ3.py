# Question: Create a Parent and Child Classes for Employees
# Definition: Create a parent class Employee with attributes name and employee_id, and a child class Manager that inherits from Employee and has an additional attribute department.

   
# Sample Input:
#    Enter the manager's name: Alice
#    Enter the manager's employee_ID: 12345
#    Enter the manager's department: Sales
   

# Sample Output:
#    Manager Details:
#    Name: Alice
#    Employee ID: 12345
#    Department: Sales
   

class Employees():
    def __init__(self,name,employee_ID):
        self.name=name
        self.employee_ID=employee_ID

class Manager(Employees):
    def __init__(self, name, employee_ID,department):
        super().__init__(name, employee_ID)
        self.department=department

Manager1=Manager("Alice",12345,"Sales")
print(f'''Manager Details:
Name:{Manager1.name}
Employee_ID;{Manager1.employee_ID}
Department:{Manager1.department}''')


