# src/bank_operations.py

from M13.src_hw.bank_account import BankAccount

def transfer(source_account, destination_account, amount):
    if amount <= 0:
        raise ValueError("Сумма перевода должна быть больше нуля")
    if source_account.balance < amount:
        raise ValueError("Недостаточно средств на счёте источника")
    
    source_account.withdraw(amount)
    destination_account.deposit(amount)