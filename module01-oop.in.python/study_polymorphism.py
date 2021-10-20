from random import random

from banking.domain import Account, CheckingAccount

acc1 = None
if random() < 0.5:
    print("head")
    acc1 = Account("tr1", 5000)
else:
    print("tail")
    acc1 = CheckingAccount("tr2", 5000, 1000)
acc1.withdraw(500)  # polymorphic method
print(acc1)
