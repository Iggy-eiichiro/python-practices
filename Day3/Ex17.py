class Engine:
    def start(self):
        print("Engine started")


class Car:# Car has the Engine, so "class Car" is natural more than "class Car(Engine)
    def __init__(self):
        self.engine = Engine()#class Engine comr to here


car = Car()

car.engine.start()# take the engine inside of the car,after that, take start() inside of the engine