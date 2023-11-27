class Duck():
    def swim(self):
        print("i am duck i can swim")

    def speak(self):
        print("Quak Quak")

class dog():
    def swim(self):
        print("i am dog i can swim")

    def speaks(self):
        print("woof wooof")

def display(dog1):
    dog1.swim()
    dog1.speaks()
    print("infomation done")

# duck1=Duck()
# display(duck1)
dog1=dog()
display(dog1)



