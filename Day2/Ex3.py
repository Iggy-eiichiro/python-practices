def validate_int(func): # the function takes another function
    def wrapper(x):#wrapper is function that works when it takes certain order, for now, which is double(5)
        if not isinstance(x,int):# isinstance() is a function that returns True or False
            raise TypeError("Expected int")

        return func(x)# Return, which mean you have got answer.
    return wrapper# Return, which mean you have got answer.

@ validate_int
def double(x):
    return x*2

print(double(5)) # 5 is integer, so it's not gonna happen error
try: 
   print(double("5")) #"5" of "" is not integer, string, so it's gonna happen TypeError
except TypeError as e:
    print(e)


