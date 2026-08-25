class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    


vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = Vector(15, 30)
vector4 = Vector(17, 34)

result = vector1 + vector2# + vector3 + vector4

print(result)

# The system go proceed just one by one.
# put 3 vectors in calculate system,  3rd vector would be calculated after calculate vector1 + vector2