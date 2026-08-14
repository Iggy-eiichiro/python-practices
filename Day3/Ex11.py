class Person:

    @staticmethod# no need objects, because just want make sure about age
    # no access to data, no take self
    def is_adult(age):#"is _" response with True or False
        return age >= 18


print(Person.is_adult(20))