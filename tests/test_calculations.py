import py
import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, value", [
    (3, 2, 5), (4, 8, 12), (7, 1, 8), (12, 4, 16)
])
def test_add(num1, num2, value):
    print("'Testing add function'")
    
    assert add(num1, num2) == value

def test_subtract():
    assert subtract( 9, 4) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(30, 6) == 5

def test_bank_set_initial_amount(bank_account):

    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):

    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):

    bank_account.withdraw(20)

    bank_account.balance == 30

def test_deposit(bank_account):

    bank_account.deposit(20)

    assert bank_account.balance == 70

def test_collect_interest(bank_account):

    bank_account.collect_interest()

    assert round(bank_account.balance, 2) == 55


@pytest.mark.parametrize("deposited, withdrew, balance", [
    (200, 100, 100), (50, 10, 40), (1200, 300, 900), (15000, 4000, 11000), 
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, balance):

    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)

    assert zero_bank_account.balance == balance

def test_insufficient_funds(bank_account):
    
    with pytest.raises(InsufficientFunds):

        bank_account.withdraw(200)