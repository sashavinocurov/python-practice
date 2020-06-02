from bank import *
class User:
    def __init__(self, name):
        self.name = name
        # self.email = email
        self.account = BankAccount("VTB", 0.25, 1000000)
    
    def make_deposit(self, amount):
        if amount>0:
            self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        if amount >0:
            self.account.withdraw(amount)
        return self
    # def transfer_money(self, amount, other_user):
    #     if amount>0:
    #         self.account -= amount
    #         other_user.account += amount

    def display_user_balance(self):
        self.account.display_account_info()
        return self

guido=User("Guido van Rossum")

# mike=User("Mike Vazovskiy", 0)
# sasha=User("Sasha Vin",2000)
guido.display_user_balance()
guido.make_deposit(100).display_user_balance()
# mike.make_deposit(100).make_withdraw(50).make_deposit(100).make_withdraw(25).display_user_balance()
# sasha.make_deposit(10000).make_withdraw(500).make_withdraw(1500).make_withdraw(2500).display_user_balance()
# sasha.transfer_money(100, mike)
# sasha.display_user_balance()
# mike.display_user_balance()
