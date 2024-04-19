
# # https://replit.com/@codewithharry/69-Day-69-Class-Methods#.tutorial/Tutorial.md
# # Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class 
# # in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors 
# # for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

## example to change the class variables 
# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany

# e1 = Employee()
# e1.name = "Noor"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)

## example to get new class instance with a changed constructor 

class Student:
    
    noOfStudents = 1200
    def __init__(self, colName) :
       self._colName = colName
       
    @classmethod
    def changeCollege(cls, newCollege):
        return cls(newCollege)

s1 = Student("REVA")
print(s1._colName)
s2 = s1.changeCollege("NEU")
print(s2._colName)
print(s2.noOfStudents)
