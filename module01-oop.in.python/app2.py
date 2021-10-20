from banking.domain import Account, InsufficientBalanceError

try:
    acc1 = Account("tr1", 10000)
    print(acc1)
    acc1.deposit(2000)
    print(acc1)
    acc1.withdraw(8000)
    print(acc1)
    acc1.withdraw(4001)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"Error has occurred: {err.message}")
    print(f"Deficit: {err.deficit}")
