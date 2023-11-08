class human():
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")


class male(human):
    def flirt(self):
        print("i can flart")
    def work(self):
        super().work()
        print("i can code")

male1=male()
male1.eat()
male1.flirt()
male1.work()