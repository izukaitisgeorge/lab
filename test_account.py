import pytest
from account import *


class Test:
    def test_init(self):
        self.test_account = Account('John')
        assert self.test_account.get_name() == 'John'
        assert self.test_account.get_balance() == 0

    def test_deposit(self):
        assert self.test_account

    def test_withdrawal(self):

