from logging import raiseExceptions


class Account():
    def __init__(self, id, balance):
        self.id = id

        if balance < 0:
            raise Exception("Invalid")
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= self.amount
        return self.balance

    def deposit(self, amount):
        self.balance += self.amount
        return self.balance

    def get_balance(self, balance):
        return self.balance
    # def get_bank_routing_number(self, bank):
