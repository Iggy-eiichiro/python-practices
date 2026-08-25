age = int(input("Please enter your age:"))

if age < 0:
    raise ValueError("Age cannot be negative")

else:
    print(f"age:{age}")