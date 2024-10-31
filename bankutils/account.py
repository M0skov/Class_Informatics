class BankAccount:
    def __init__(self, initial_balance = 0):
        if initial_balance < 0:
            raise ValueError("Amount must be positive")
        else:
            self.current_balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError( "Invalid Amount")
        self.current_balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawl cannot be negative")
        elif amount > self.current_balance:
            raise ValueError("Insufficeint funds")
        self.current_balance -= amount
    def check_balance(self):
        return "Your current balance is:" + str(self.current_balance)
    def __str__(self):
        return "Bank account: current Balance:$" + str(self.current_balance)
    
class SavingsAccount:
    def __init__(self, initial_balance=0, interest_rate=0.02):
        if initial_balance < 0:
            raise ValueError("Amount must be positive")
        self.current_balance = initial_balance
        self.interest_rate = interest_rate
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid Amount")
        self.current_balance += amount
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Withdrawl cannot be negative")
        elif amount > self.current_balance:
            raise ValueError("Insufficeint funds")
        self.current_balance -= amount
    def check_balance(self):
        return "Your current Balance is:"+ str(self.current_balance)
    def apply_interest(self):
        new_rate = self.current_balance*self.interest_rate
        self.deposit(new_rate)
    def __str__(self):
        return "Saving Account-Current Balance is:"+ str(self.current_balance)



