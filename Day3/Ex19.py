import json
class User:
    def __init__(self,name):
        self.name = name

    def to_dict(self):
        return{"name": self.name }

user = User("Eiichiro")

print(json.dumps(user.to_dict()))