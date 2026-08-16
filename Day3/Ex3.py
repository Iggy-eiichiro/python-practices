class Account:
    def __init__(self, balance):# init is preparation process that is automatically executed when you create a new one from Class. for now, get 1000.
        self.__balance = balance


acc = Account(1000)

print(acc.__balance)# __ makes the attribute name harder to access directly from outside the class.
# This is called name mangling and helps hide the attribute.