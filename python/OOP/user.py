class User:
    def __init__(self, name, balance):
        self.name = name
        # self.email = email
        self.account_balance = balance
        print("Account Created for"+" "+ self.name)
    
    def make_deposit(self, amount):
        if amount>0:
            self.account_balance += amount
        return self
    
    def make_withdraw(self, amount):
        if amount >0:
            self.account_balance -= amount
        return self
    def transfer_money(self, amount, other_user):
        if amount>0:
            self.account_balance -= amount
            other_user.account_balance += amount

    def display_user_balance(self):
        print("Balance is {}".format(self.account_balance))

guido=User("Guido van Rossum", 150)
mike=User("Mike Vazovskiy", 0)
sasha=User("Sasha Vin",2000)
guido.make_withdraw(100).make_deposit(200).make_deposit(300).make_deposit(250).display_user_balance()
mike.make_deposit(100).make_withdraw(50).make_deposit(100).make_withdraw(25).display_user_balance()
sasha.make_deposit(10000).make_withdraw(500).make_withdraw(1500).make_withdraw(2500).display_user_balance()
sasha.transfer_money(100, mike)
sasha.display_user_balance()
mike.display_user_balance()
