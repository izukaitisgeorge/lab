import pytest
from account import *


class Test:
    def test_init(self):
        self.test_account = Account('John')
        assert self.test_account.get_name() == 'John'
        assert self.test_account.get_balance() == 0

    def test_deposit(self):
        assert self.test_account.deposit(1.1) == True
        assert self.test_account.deposit(0) == False
        assert self.test_account.deposit(-1) == False

    def test_withdrawal(self):
         assert self.test_account.deposit(1.1) == True
        assert self.test_account.deposit(0) == False
        assert self.test_account.deposit(-1) == False

