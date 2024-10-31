from bankutils import BankAccount
from bankutils import SavingsAccount
if __name__ == "__main__":
#Bank Account Test Case
    try:
        account= BankAccount(-200) # expected error message
    except ValueError as e:
        print(e)
    else:
        print(account)
    account = BankAccount(200)
    account.deposit(50)
    print(account)# Expected balance: $250
try:
    account.withdraw(-200) # expected error message
except ValueError as e:
    print(e)
try:
    account.withdraw(300) # Expected: "Insufficient balance"
except ValueError as e:
    print(e)    
account.withdraw(100)
print(account) # Expected balance: $150

#SavingsAccount Test Case
if __name__ == "__main__":
    try:
        Sav_account= SavingsAccount(200,.02) # 2% interest rate
    except ValueError as e:
        print(e)
Sav_account.deposit(100) 
Sav_account.apply_interest() # Expected balance after interest: $306
print(Sav_account) 
try:
    Sav_account.withdraw(-200) # expected error message
except ValueError as e:
    print(e)
try:
    Sav_account.withdraw(500) # Expected: "Insufficient balance"
except ValueError as e:
    print(e)    
Sav_account.withdraw(50)
print(Sav_account)