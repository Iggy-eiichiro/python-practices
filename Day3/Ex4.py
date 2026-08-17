class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter#  setter of proccess for changing value
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


age = int(input("please give me your age:"))

person = Person(age)

# age = int(input("please give me your age:"))

# person.age = age

print(f"age:{person.age}")