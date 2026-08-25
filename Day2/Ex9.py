def singleton(cls): # class image is box, タイ焼きの型
    instance = None #instance is real example,タイ焼きそのもの

    def wrapper(*args, **kwargs):
        nonlocal instance # nonlocal is going to use outside of variable, it's mean use "instance" here.

        if instance is None:
            instance = cls(*args, **kwargs)

        return instance

    return wrapper

#it is differnt singleton of instance and nonlocal of instance
@singleton
class MyClass:
    pass

a = MyClass()
b = MyClass()


if a is b:# : take process behind the : 
    print("Both variables point to the same memory address.")