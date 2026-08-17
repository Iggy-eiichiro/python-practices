A = int(input("Please enter the denominator number:"))
B = int(input("Please enter the numerator number:"))

try:
    result = A/B
    print(result)
except:
    print("Cannot divide by zero")