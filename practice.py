class atm():
    def __init__(self,balace):
        self.balance=balace

    def deposite(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    def widhraw(self,amount):
        self.balance=self.balance-amount
        return self.balance
    

transitions=atm(500)
print(transitions.deposite(500))

