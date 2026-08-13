class Account:
    def __init__(self, balance):
        self.__balance = balance


acc = Account(1000)

print(acc.__balance)