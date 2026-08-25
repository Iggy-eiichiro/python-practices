class Vehicle:
    def drive(self):
        print("Vehicle is moving")


class Car(Vehicle):
    pass

car = Car()
car.drive()

# 1 have a look vehicle
# 2 have a look car, Car got Vehicle
# 3 car = Car()
# 4 car.drive()
# 4-1 have a lool car → know there is no drive()
# 4-2bhave a look vehicle → know there is drive()
# 5 Run
# 6 Print

# class Car(Vehicle):  if class car and class vhovlr is opposite, it is not working
#     pass

# class Vehicle:
#     def drive(self):
#         print("Vehicle is moving")
