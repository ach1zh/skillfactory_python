# src/bank_account.py

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть больше нуля")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счету")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance