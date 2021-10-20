from banking.domain import InsufficientBalanceError, CheckingAccount

try:
    acc1 = CheckingAccount("tr1", 1000, 1000)
    print(acc1)
    acc1.deposit(2000)
    print(acc1)
    acc1.withdraw(4000)
    print(acc1)
    acc1.withdraw(1)
    print(acc1)
except ValueError as err:
    print(err)
except InsufficientBalanceError as err:
    print(f"Error has occurred: {err.message}")
    print(f"Deficit: {err.deficit}")
