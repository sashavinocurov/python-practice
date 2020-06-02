import datetime
import pytz


class Account:
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account Created for" + " " + self._name)

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
            self._transaction_list.append((Account._current_time(), -amount))
        else: 
            print("The amount must be greater than zero and no more then your account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance)) 

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type= "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    sasha = Account("Sasha", 0)
    sasha.show_balance()

    sasha.deposit(1000)
    # sasha.show_balance()
    sasha.withdraw(500)
    # sasha.show_balance()

    sasha.withdraw(5000)

    sasha.show_transactions()

    steph = Account("Stheph", 0)
    # steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(20)
    steph.show_transactions()
    # steph.show_balance()
    # print(steph.__dict__)
    # steph._Account__balance = 40
    # steph.show_balance()
    steph.withdraw(20).deposit(50).show_transactions()