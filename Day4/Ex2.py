# A = int(input("Please enter words:")) if it is located here, it is not working correctly

try:
    A = int(input("Please enter words:"))
    value = A
    print(value)

except(ValueError,TypeError):
    print("Invalid input")
