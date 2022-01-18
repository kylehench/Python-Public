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

Beth = BankAccount()
John = BankAccount()

Beth.deposit(20).deposit(30).deposit(5).withdraw(7).yield_interest().display_account_info()
John.deposit(30).deposit(15).withdraw(1).withdraw(1).withdraw(1).withdraw(1).yield_interest().display_account_info()