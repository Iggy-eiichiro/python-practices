class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self,name,age,parent_name):
        self.name = name
        self.age = age
        self.parent_name = parent_name


child = Child(name = "Eiichiro" , age = 22, parent_name = "Takayuki")

print(f"Parent Name:{child.parent_name}")
print(f"Name:{child.name}")
print(f"Age:{child.age}")


