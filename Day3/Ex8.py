class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):# __str__ is the display method of objects that can be summarized in one place
             return f"User:{self.name}(ID:{self.user_id})"


# def __str__(self):-Here is not working , because outside of calss User
#     return f"User:{self.name}(ID:{self.user_id})"

user = User(name = "Eiichiro" , user_id = "23A2032")

print(user)
