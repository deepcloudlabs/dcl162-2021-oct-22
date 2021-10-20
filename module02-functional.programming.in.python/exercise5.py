from functools import reduce

from banking.domain import Account, CheckingAccount

accounts = [
    Account("tr1", 5000),
    CheckingAccount("tr2", 5000, 1000),
    Account("tr3", 3000),
    CheckingAccount("tr4", 4000, 500)
]

# total balance
print(reduce(lambda s, b: s + b, map(lambda acc: acc.balance, accounts), 0))

# number of Account objects
topla = lambda s, n: s + n
to_1 = lambda acc: 1
is_Account = lambda acc: type(acc) == Account

print(reduce(topla, map(to_1, filter(is_Account, accounts)), 0))

# { 'Account': 2, 'CheckingAccount': 2}
