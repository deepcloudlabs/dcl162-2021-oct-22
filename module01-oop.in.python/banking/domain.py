class InsufficientBalanceError(Exception):  # inheritance
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Account:
    def __init__(self, iban, balance):
        self._iban = iban
        self._balance = balance

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:  # validation
            raise ValueError("amount must be positive")
        if amount > self._balance:  # business rule
            deficit = amount - self._balance
            raise InsufficientBalanceError("your balance does cover your expenses", deficit)
        self._balance = self._balance - amount

    def deposit(self, amount):
        if amount <= 0:  # validation
            raise ValueError("amount must be positive")
        self._balance = self._balance + amount

    def __str__(self):
        return f"Account [iban: {self._iban}, balance: {self._balance}]"
