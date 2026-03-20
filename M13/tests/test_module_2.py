import unittest
from src.module_2 import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Метод setUp вызывается перед каждым тестом."""
        self.account = BankAccount(100)  # Начальный баланс для каждого теста

    def tearDown(self):
        """Метод tearDown вызывается после каждого теста."""
        self.account = 0 # Очищаем счёт после завершения теста

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 200)


if __name__ == '__main__':
    unittest.main()