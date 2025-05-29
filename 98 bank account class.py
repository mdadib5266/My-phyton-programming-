class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f'{amount} is deposited. current balance: {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print(f'{amount} taka has been credited . current balance: {self.balance}')

account = BankAccount()
account.deposit(float(input('deposit: ')))
account.withdraw(float(input('withdraw: ')))