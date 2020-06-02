class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name= name
        self.int_rate = int_rate
        self.account_balance = balance
        print("Bank "+self.name)
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            # self.display_account_info()
        return self
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            # self.display_account_info()
        else:
            print("The amount must be greater than zero or account balance.")
        return self
    
    def display_account_info(self):
        print("Balance is ${}".format(self.account_balance))
    
    def yield_interest(self):
        procenty = self.account_balance * self.int_rate 
        print("PROCENT " + str(procenty))
        return self

# chase = BankAccount("Chase", 0.05, 1000)
# chase.deposit(100).deposit(100).deposit(100).withdraw(10).yield_interest().display_account_info()

# vtb = BankAccount("VTB", 0.25, 1000000)
# vtb.deposit(2).deposit(2).withdraw(100000).withdraw(100000).withdraw(100000).withdraw(100000).yield_interest().display_account_info()