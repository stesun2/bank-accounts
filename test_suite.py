import unittest
from modules.account import Account


class BankTestSuite(unittest.TestCase):
    pass

class AccountTestSuite(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        a1 = Account()

    def test_create_check_initial_balance(self):
        initial_balance = 500
        a = Account(1, initial_balance)
        self.assertEqual(a.get_balance(), initial_balance)
    
    def test_create_withdraw(self):
        initial_balance = 500
        a = Account(1, initial_balance)

        withdraw_amount = 100
        new_balance = a.withdraw(withdraw_amount)
        self.assertEqual(new_balance, 400)

if __name__ == '__main__':
    unittest.main()