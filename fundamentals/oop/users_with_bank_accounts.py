class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

Guido = User('Guido van Rossum')
Joe = User('Joe')
Frank = User('Frank')

Guido.make_deposit(100).make_deposit(20).make_deposit(70).make_withdrawal(5).display_user_balance()

Joe.make_deposit(10000).make_deposit(100000).make_withdrawal(10).make_withdrawal(80).display_user_balance()

Frank.make_deposit(30).make_withdrawal(5).make_withdrawal(15).make_withdrawal(8).display_user_balance()

Guido.transfer_money(Frank, 5).display_user_balance()
Frank.display_user_balance()