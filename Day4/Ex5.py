class InsufficientFundsError(Exception):# if there is no InsufficientFundsError() it is not working, because there is no exist in Paython
    pass


balance = 100
withdraw = int(input("How much do you want to withdraw:"))


if withdraw <= balance:
    balance -= withdraw
    print(f"Withdraw:{withdraw}")
    print(f"Bslance:{balance}")

else:
    raise InsufficientFundsError("Not enough money")


