from abc import ABC, abstractmethod# it is mean bring abstractmethod


class Shape(ABC):

    @abstractmethod# it is  just making base for geometric shape 
    def area(self):
        pass
#if there is @abstractmethod, need to attach area()

shape = Shape()