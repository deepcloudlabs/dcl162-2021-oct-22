import pytest

from banking.domain import Account, InsufficientBalanceError, CheckingAccount


@pytest.fixture
def an_account():
    return Account("tr1", 1000)


@pytest.fixture
def a_checking_account():
    return CheckingAccount("tr2", 2000, 1000)


def test_create_a_checking_account_successfuly(a_checking_account):
    assert a_checking_account.iban == "tr2"
    assert a_checking_account.balance == 2000
    assert a_checking_account.overdraft_amount == 1000


def test_checking_withdraw_with_negative_amount_then_raises_value_error(a_checking_account):
    with pytest.raises(ValueError):
        a_checking_account.withdraw(-1)
    assert a_checking_account.balance == 2000


def test_create_an_account_successfuly(an_account):
    """
    creates an account
    """
    # 2. Call exercise method: __init__
    # 3. verification
    assert an_account.iban == "tr1"
    assert an_account.balance == 1000
    # 4. Tear-down: No operation


def test_deposit_with_negative_amount_then_raises_value_error(an_account):
    # 2. Call exercise method: deposit
    with pytest.raises(ValueError):
        an_account.deposit(-1)
    assert an_account.balance == 1000


def test_deposit_with_positive_amount_then_success(an_account):
    # 2. Call exercise method: deposit
    an_account.deposit(1)
    # 3. verification
    assert an_account.balance == 1001
    # 4. Tear-down


def test_withdraw_with_negative_amount_then_raises_value_error(an_account):
    # 2. Call exercise method: withdraw
    with pytest.raises(ValueError):
        an_account.withdraw(-1)
    assert an_account.balance == 1000


def test_withdraw_with_over_balance_then_raises_insufficient_balance(an_account):
    # 2. Call exercise method: withdraw
    with pytest.raises(InsufficientBalanceError):
        an_account.withdraw(1001)
    assert an_account.balance == 1000


def test_withdraw_with_all_balance_then_success(an_account):
    # 2. Call exercise method: withdraw
    an_account.withdraw(1000)
    # 3. verification
    assert an_account.balance == 0
