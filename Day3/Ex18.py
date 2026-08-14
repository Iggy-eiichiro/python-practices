class Calculator:
    def __call__(self, x):
        return x * 2


my_obj = Calculator()

print(my_obj(5))