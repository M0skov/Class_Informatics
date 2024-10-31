from bankutils import BankAccount
from bankutils import SavingsAccount

#Bank Account Test Case
account= BankAccount(-200) # expected error message
account = BankAccount(200)
account.deposit(50)
print(account)# Expected balance: $250
account.withdraw(300) # Expected: "Insufficient balance"
account.withdraw(100)
print(account) # Expected balance: $200
#SavingsAccount Test Case
savings = SavingsAccount(200, 0.02) # 2% interest rate
savings.deposit(100) # Expected balance: $300
savings.apply_interest() # Expected balance after interest: $315
print(savings) # Expected output: $31
if __name__ == "__main__":
    main()