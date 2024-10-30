class BankAccount:
    def __init__(self, initial_balance = 0):
        if initial_balance < 0:
            raise ValueError("Amount must be positive")
        else:
            self.current_balance = initial_balance
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid input")
        else:
            self.current_balance += amount
    def withdraw(self, amount):
        if amount > self.current_balance:
            return "Insufficeint funds"
        else:
            self.current_balance -= amount
    def check_balance(self):
        return "Your current balance is:" + str(self.current_balance)
    def __str__(self):
        return self.current_balance
    
    class SavingsAccount:
        def __init__(self, initial_balance=0, interest_rate=0.02):
            if initial_balance <= 0:
                return ValueError("Amount must be positive")
            else:
                self.current_balance = initial_balance
                self.interest_rate = interest_rate
        def deposit(self, amount):
            if amount < 0:
                return ValueError("Invalid Amount")
            else:
                self.current_balance=+amount
        def withdraw(self,amount):
            if amount > self.current_balance:
                return ValueError("Insufficient funds")
            else:
                self.amount -= amount
        def check_balance(self):
            return "Your current Balance is:"+ str(self.current_balance)
        def apply_interest(self):
            self.current_balance*=(1+self.interest_rate)
            return self.current_balance
        def __str__(self):
            return "Saving Account-Current Balance is:"+ str(self.current.balance)

