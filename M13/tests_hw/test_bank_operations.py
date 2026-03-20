"""
Тестирование функции transfer:
Тестирование успешного перевода средств между счетами.
Тестирование исключения при попытке перевода суммы, превышающей баланс.
Тестирование исключения при попытке перевода нулевой или отрицательной суммы.
"""

import unittest
from M13.src_hw.bank_account import BankAccount
from M13.src_hw.bank_operations import transfer

class MyTest(unittest.TestCase):
    
    def setUp(self):
        """Метод setUp вызывается перед каждым тестом."""
        self.account_1 = BankAccount(99,100)  # Начальный баланс для каждого теста
        self.account_2 = BankAccount(11,100)

    def tearDown(self):
        """Метод tearDown вызывается после каждого теста."""
        self.account_1 = 0 # Очищаем счёт после завершения теста    
        self.account_2 = 0

    def test_withdraw(self):
        transfer(self.account_1, self.account_2,10)
        self.assertEqual(self.account_1.get_balance(), 90)
        self.assertEqual(self.account_2.get_balance(), 110)    
    
    def test_ex_transfer_1(self):        
        self.assertRaises(Exception,transfer,self.account_1, self.account_2, 10000)    
    
    def test_ex_transfer_2(self):        
        self.assertRaises(ValueError,transfer,self.account_1, self.account_2, -10)
    
    def test_ex_transfer_3(self):        
        self.assertRaises(ValueError,transfer,self.account_1, self.account_2, 0)    

if __name__ == '__main__':
    unittest.main()

"""
В ответе используется with. Нужно раскурить подробнее про это.

    def test_transfer_exceeds_balance(self):
        ""Тестирование перевода суммы, превышающей баланс счета источника.""
        with self.assertRaises(ValueError):
            transfer(self.source_account, self.destination_account, 1500)

    def test_transfer_negative_amount(self):
        ""Тестирование попытки перевода отрицательной суммы.""
        with self.assertRaises(ValueError):
            transfer(self.source_account, self.destination_account, -100)
"""