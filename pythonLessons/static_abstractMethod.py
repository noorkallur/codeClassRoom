# # STATIC METHOD
# # static method doesnot belong to a class or instance it resides in a class, it use to ship a functionality with the class and hence can be used a part of the class
# class student:
#     def __init__(self, name, age) :
#         self._name = name
#         self._age = age
    
#     @staticmethod
#     def minimumAgeMet(age): # does not take self
#        return True if age > 18 else False

# Ann = student("Ann", 19)
# print(student.minimumAgeMet(17))
# print(Ann.minimumAgeMet(16))

# # ABSTRACTION
# # there is no direct topic of abstraction, but abc module has @abstractmethod decorator for creating the same
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def noOfSides(self):
        pass
class Rectangle(shape):
    def __init__(self, breadth, length):
        self._breadth = breadth
        self._length = length
    def noOfSides(self): # if you dont include noOfSides , throws an error at creation of Rectangel object
        return 4
        
r = Rectangle(5, 6)