class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

Guido = User('Guido van Rossum')
Joe = User('Joe')
Frank = User('Frank')

Guido.make_deposit(100)
Guido.make_deposit(20)
Guido.make_deposit(70)
Guido.make_withdrawal(5)
Guido.display_user_balance()

Joe.make_deposit(10000)
Joe.make_deposit(100000)
Joe.make_withdrawal(10)
Joe.make_withdrawal(80)
Joe.display_user_balance()

Frank.make_deposit(30)
Frank.make_withdrawal(5)
Frank.make_withdrawal(15)
Frank.make_withdrawal(8)
Frank.display_user_balance()

Guido.transfer_money(Frank, 5)
Guido.display_user_balance()
Frank.display_user_balance()