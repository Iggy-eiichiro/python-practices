class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod# classmethod take "cls" automatically
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


person = Person.from_string("Alex-25")

print(person.name)
print(person.age)

#  @staticmethod organize the information without class data, without objects method(user = user() etc,)
#  @classmethod organize the information, using inside of class data



# no need to write like below code 

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def from_string(self, data):
#         name, age = data.split("-")
#         self.name = name
#         self.age = int(age)

# person = Person("", 0)

# person.from_string("Alex-25")

# print(person.name)
# print(person.age)