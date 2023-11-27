# Assignment: Banking System with Bank Branch, Account Operations, and Account Holders

# Task 1: Create a class called `AccountHolder` with the following attributes:
#   - name (string)
#   - address (string)
#   - contact_number (string)

# Task 2: Implement a constructor (__init__ method) that initializes the attributes.

# Task 3: Create a class called `Account` with the following attributes:
#   - account_number (string)
#   - account_holder (AccountHolder object)
#   - balance (float)

# Task 4: Implement a constructor (__init__ method) that initializes the attributes.

# Task 5: Implement a method called `display_balance` in the `Account` class that prints the account balance.

# Task 6: Implement a method called `deposit` in the `Account` class that takes an amount as a parameter and adds it to the balance.

# Task 7: Implement a method called `withdraw` in the `Account` class that takes an amount as a parameter and subtracts it from the balance.

# Task 8: Create a class called `BankBranch` with the following attributes:
#   - branch_name (string)
#   - accounts (a list to store Account objects)

# Task 9: Implement a constructor (__init__ method) that initializes the attributes.

# Task 10: Implement a method called `add_account` in the `BankBranch` class that adds an Account object to the list of accounts.

# Task 11: Implement a method called `display_accounts` in the `BankBranch` class that prints the details of all accounts associated with the branch.

# Task 12: Create instances of the `AccountHolder`, `Account`, and `BankBranch` classes and demonstrate their functionality by performing account operations and displaying account details.


# account_holder1 = AccountHolder("John Doe", "123 Main St", "555-1234")
# account_holder2 = AccountHolder("Jane Smith", "456 Oak St", "555-5678")

# account1 = Account("123456", account_holder1, 1000.0)
# account2 = Account("789012", account_holder2, 2000.0)

# main_street_branch = BankBranch("Main Street Branch")

# main_street_branch.add_account(account1)
# main_street_branch.add_account(account2)

# main_street_branch.display_accounts()

# account1.deposit(500.0)
# account2.withdraw(300.0)




class AccountHolder():
    def __init__(self,name,Address,Contact_No):
        self.Name=name
        self.Address=Address
        self.Contact_no=Contact_No

class Account(AccountHolder):
    def __init__(self, name, Address, Contact_No,Ac_no,Acc_holder,balance):
        super().__init__(name, Address, Contact_No)
        self.account_number=Ac_no
        self.account_holder=Acc_holder
        self.balance=balance

    def display_balance(self):
        return self.balance

    def deposit(self,amount):
        self.amount=amount
        self.balance= self.balance + self.amount
        return ("deposite_done Avilable Balance:-"), self.balance

    def withdraw(self,amount):
        self.amount=amount
        self.balance= self.balance-self.amount
        return ("widhraw_done Avilable Balance:-",self.balance)


# Task 8: Create a class called `BankBranch` with the following attributes:
#   - branch_name (string)
#   - accounts (a list to store Account objects)

class BankBranch(Account):
    def __init__(self, name, Address, Contact_No, Ac_no, Acc_holder, balance,branch_name):
        super().__init__(name, Address, Contact_No, Ac_no, Acc_holder, balance)
        self.branch_name=branch_name


# Task 10: Implement a method called `add_account` in the `BankBranch`
#  class that adds an Account object to the list of accounts.
    
    def add_account(self,accounts):
        self.account=accounts
        return 
    
    def display_accounts(self):
        return (f"""Account Details:-
name:-{self.Name}
Address:-{self.Address}
Contact_No:-{self.Contact_no}
Ac_no:-{self.account_number}
Acc_holder:-{self.account_holder}
balance:-{self.balance}
branch_name:-{self.branch_name}""")


person1=BankBranch("John Doe", "123 Main St", "555-1234","123456", "account_holder1", 1000.0,"Main Street Branch")


print(person1.display_accounts())
