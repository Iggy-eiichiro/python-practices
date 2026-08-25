students = [{'Sena':1},{'Hesun':2},{'Eiichiro':3},{'Kokoro':4},{'Quang':5},{'Nhung':6}]


class Student:
    def __init__(self, name, classnumber):
        self.name = name
        self.number = classnumber

    def show(self):
        print("Name:", self.name)
        print("Classnumber:", self.number)


for i in range(len(students)):
    name = list(students[i].keys())[0]
    print(i + 1, ":", name)


number = int(input("Please choose the student number: "))


item = students[number - 1]

name = list(item.keys())[0]
classnumber = list(item.values())[0]


s = Student(name, classnumber)


s.show()