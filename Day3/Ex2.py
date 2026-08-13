students = [
    {'name': 'Sena', 'classnumber': 1, 'score': 5},
    {'name': 'Hesun', 'classnumber': 2, 'score': 5},
    {'name': 'Eiichiro', 'classnumber': 3, 'score': 2},
    {'name': 'Kokoro', 'classnumber': 4, 'score': 4},
    {'name': 'Quang', 'classnumber': 5, 'score': 5},
    {'name': 'Nhung', 'classnumber': 6, 'score': 3}
]


class Student:
    def __init__(self, name, classnumber,score):
        self.name = name
        self.number = classnumber
        self.score = score


    def show(self):
        print(f"student name:{self.name}")
        print(f"student classnumber:{self.number}")
        print(f"student score:{self.score}")


for i in range(len(students)):
    name = students[i]['name']
    print(i + 1, ":", name)


number = int(input("Please choose the student number: "))
                

name = students[number-1]['name']
classnumber =  students[number-1]['classnumber']
score = students[number-1]['score']


s = Student(name, classnumber, score)


s.show()

if students[number-1]['score'] <= 3:
    print("Failed")
else:
    print("Passed")
