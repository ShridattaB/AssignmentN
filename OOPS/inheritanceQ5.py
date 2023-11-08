# Question: Create a Hierarchy of Electronic Devices
# Definition: Create a parent class ElectronicDevice with attributes brand and model. Then, create two derived classes, Smartphone and Laptop, that inherit from ElectronicDevice and have additional attributes, such as operating_system and screen_size.

   
# Sample Input:
#    Enter the smartphone brand: Apple
#    Enter the smartphone model: iPhone 13
#    Enter the smartphone operating system: iOS
#    Enter the laptop brand: Dell
#    Enter the laptop model: XPS 15
#    Enter the laptop screen size (in inches): 15.6
   

#    -
#  Sample Output:
     
#  Smartphone Details:
#      Brand: Apple
#      Model: iPhone 13
#      Operating System: iOS

#      Laptop Details:
#      Brand: Dell
#      Model: XPS 15
#      Screen Size: 15.6 inches
   
# Explanation:
# Define a parent class ElectronicDevice with brand and model attributes.
# Create two child classes, Smartphone and Laptop, inheriting from ElectronicDevice and adding attributes specific to each device.
# Prompt the user to input details for a smartphone and a laptop, create instances for each class, and display their respective details, including the operating system for smartphones and the screen size for laptops.


class ElectronicDevice():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Smartphone(ElectronicDevice):
    def __init__(self, brand, model,operating_system):
        super().__init__(brand, model)
        self.operation_sysytem=operating_system

class laptop(ElectronicDevice):
    def __init__(self, brand, model, Screen_Size):
        super().__init__(brand, model)
        self.Screen_Size=Screen_Size

smartphone1=Smartphone("Apple","iPhone_13","iOS")
print(f"SmartPhone Details :\nBrand:{smartphone1.brand}\nModel:{smartphone1.model}\nOperating_system:{smartphone1.operation_sysytem}\n")

laptop1=laptop("Dell","XPS 15","15.6 inches")
print(f"Laptop_details\nBrand:{laptop1.brand}\nmodel:{laptop1.model}\nScreen_size:{laptop1.Screen_Size}")





