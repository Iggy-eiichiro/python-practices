def make_adder(n): # get the number 5
    def adder(x): # get the number 10
        return x + n

    return adder


add_five = make_adder(5)

print(add_five(10))