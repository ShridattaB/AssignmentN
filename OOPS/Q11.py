# Question 6: Create a class BankAccount with attributes account_number and balance. 
# Add a method deposit to increase the balance and a method withdraw to decrease the balance. 
# Create an object and perform deposit and withdrawal operations.

#    Sample Input:
   
#    account = BankAccount("12345", 1000)
#    account.deposit(500)
#    account.withdraw(300)
   
#    Sample Output:
   
#    Updated Balance: 1200
#    Explanation: This question involves creating a class for a bank account
#   and performing deposit and withdrawal operations on it.

class BankAccount():
    def __init__(self,Ao,Balance):
        self.Account_number=Ao
        self.Balace=Balance

     

    def deposite(self,amount):
        self.Balace=self.Balace+amount
        return self.Balace

    def widhdrew(self,amount):
        self.Balace=self.Balace-amount
        return self.Balace
    
    def check_balace(self):
        print(self.Balace)

account=BankAccount("12345", 1000)
print(account.deposite(500))
print(account.widhdrew(200))
account.check_balace()


