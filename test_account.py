import pytest
from account import Account


def test_account_init():
    account = Account("Jim")
    assert account.get_name() == "Jim"
    assert account.get_balance() == 0


def test_account_deposit():
    account = Account("Jim")
    assert account.deposit(50) is True
    assert account.get_balance() == 50
    assert account.deposit(-10) is False
    assert account.get_balance() == 50


def test_account_withdraw():
    account = Account("Jim")
    account.deposit(70)
    assert account.withdraw(50) is True
    assert account.get_balance() == 20
    assert account.withdraw(100) is False
    assert account.get_balance() == 20

    
  
    
