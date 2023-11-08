# Question: Create a Base Class and Two Derived Classes
# Definition: Create a base class named Animal with attributes name and species. Then, create two derived classes, Dog and Cat, that inherit from Animal and add specific attributes.

# Sample Input:
#    Enter the dog's name: Max
#    Enter the dog's breed: Labrador
#    Enter the cat's name: Whiskers
#    Enter the cat's color: Gray
  
# Sample Output:

     
# Dog Details:
#      Name: Max
#      Species: Canine
#      Breed: Labrador

#      Cat Details:
#      Name: Whiskers
#      Species: Feline
#      Color: Gray

# Explanation:
# Define a base class Animal with name and species attributes.
# Create two child classes, Dog and Cat, inheriting from Animal. Add specific attributes for each, such as breed for dogs and color for cats.
# Prompt the user to input details for a dog and a cat, create instances for each class, and display their respective details.\


class Animal():
    def __init__(self,name,species):
        self.name=name
        self.species=species

class dog(Animal):
    def __init__(self, name, species,breed):
        super().__init__(name, species)
        self.breed=breed

class cat(Animal):
    def __init__(self, name, species,colour):
        super().__init__(name, species)
        self.colour=colour

    
dog1=dog("Max","Canine","Labrador")
print(f"Dog_detail\nName:{dog1.name}\nSpecies:{dog1.species}\nBreed:{dog1.breed}\n")

cat1=cat("Whiskers","Feline","Greay")
print(f"cat_detail\nName:{cat1.name}\nspecies:{cat1.species}\nColour{cat1.colour}")



