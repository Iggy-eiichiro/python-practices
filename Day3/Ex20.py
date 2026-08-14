class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1


user1 = User("A")
user2 = User("B")
user3 = User("C")
user1 = User("A")

print(User.count)