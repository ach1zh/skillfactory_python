"""
Тестирование класса BankAccount:
Тестирование инициализации счёта с начальным балансом.
Тестирование депозита положительной суммы.
Тестирование снятия суммы, не превышающей баланс.
Тестирование исключений для недопустимых операций депозита и снятия средств.
"""

import unittest
from M13.src_hw.bank_account import BankAccount


class MyTest(unittest.TestCase):
    
    def setUp(self):
        """Метод setUp вызывается перед каждым тестом."""
        self.account = BankAccount(99,100)  # Начальный баланс для каждого теста

    def tearDown(self):
        """Метод tearDown вызывается после каждого теста."""
        self.account = 0 # Очищаем счёт после завершения теста

    def test_account_initialization(self):
        """Тестирование инициализации счёта."""
        self.assertEqual(self.account.account_number, 99)
        self.assertEqual(self.account.balance, 100)
    
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 200)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)

    def test_ex_deposit(self):        
        self.assertRaises(Exception,self.account.deposit,-10)
    
    def test_ex_withdraw_1(self):        
        self.assertRaises(Exception,self.account.withdraw,-10)

    def test_ex_withdraw_2(self):        
        self.assertRaises(Exception,self.account.withdraw,10000)    

if __name__ == '__main__':
    unittest.main()    
