class Animal:
    # to put together what we have in common
    # class Animal is Base class, even without Base class,it's possible to make code but it is better with Base class
    def speak(self):
        print("Animal sound")

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()


dog.speak()
cat.speak()

dog.eat()
cat.eat()