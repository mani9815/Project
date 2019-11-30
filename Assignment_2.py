# 1. Create a class "BankAccount" which comprises-
# a. A method "Check_balance" 
# b. A method "Deposit"
# c. A method "Withdraw"

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def Deposit(self,amount):
        self.balance += amount
        
    def Withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print ("Withdraw sucessfull")
        else:
            print ("Insufficient balance")
            
    def Check_balance(self):
        print ("Balance", self.balance)
        


ATM = BankAccount()
ATM.Deposit(80000)   

ATM.Check_balance()

ATM.Withdraw(25000)

ATM.Check_balance()

ATM.Withdraw(60000)



# 2. Create another class "MinimumBalanceAccount" which inherits "BankAccount"
# a. Set minimum balance to 5000
# b. over-ride "withdraw" method to check if minimum balance is maintained


class MinimumBalanceAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.minimum_balance = 5000
        
    def withdraw(self,amount):
        if (self.balance - amount >= self.minimum_balance):
            self.balance -= amount
            print("Withdraw successfull")
        else:
            print ("Insufficient fund, Please deposit to withdraw")
            
            

ATM1 = MinimumBalanceAccount() 

ATM1.Deposit(58642)
         
ATM1.Withdraw(10000)

ATM1.Check_balance()

ATM1.withdraw(2000)




         
    
  
        
