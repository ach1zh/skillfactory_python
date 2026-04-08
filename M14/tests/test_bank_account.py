#  tests/test_bank_account.py
from M14.src.bank_account import BankAccount

def test_bank_account_initial_balance():
    account = BankAccount("1234567890")
    assert account.get_balance() == 0
