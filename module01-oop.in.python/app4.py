from banking.domain import Account, CheckingAccount


def hesap_isletim_ucreti(acc, amount):
    """
        hesap isletim ucreti al
    """
    acc.withdraw(amount)


accounts = [
    Account("tr1", 5000),
    CheckingAccount("tr2", 5000, 1000),
    Account("tr3", 3000),
    CheckingAccount("tr4", 4000, 500)
]

for acc in accounts:
    hesap_isletim_ucreti(acc, 10)  # polymorphic!
    print(acc)
