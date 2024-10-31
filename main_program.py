from bankutils import BankAccount
from bankutils import SavingsAccount

#Bank Account Test Case
account= BankAccount(-100) # expected error message
account = BankAccount(100)
account.deposit(50)
print(account)# Expected balance: $150
account.withdraw(200) # Expected: "Insufficient balance"
account.withdraw(100)
print(account) # Expected balance: $5
#SavingsAccount Test Case
savings = SavingsAccount(200, 0.02) # 5% interest rate
savings.deposit(100) # Expected balance: $300
savings.apply_interest() # Expected balance after interest: $315
print(savings) # Expected output: $31
if __name__ == "__main__":
    main()