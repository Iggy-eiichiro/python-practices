# A = int(input("Please enter words:")) if it is located here, it is not working correctly

try:
    A = int(input("Please enter words:"))
    value = A
    print(value)

except(ValueError,TypeError):
    print("Invalid input")

    #ValueError. if a function receives a value of wrong type (int("abc"))
    #TypeError. if it isconcatenated a string and a number (print("hello" + 15))
