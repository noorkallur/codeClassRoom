# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# # Use childClass(Parentclass) -> this inherits all the properties
# # use this link to glance https://www.w3schools.com/python/python_inheritance.asp
# # https://www.geeksforgeeks.org/inheritance-in-python/?ref=next_article

# class Person(object):
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name
  
# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
# 	# Here we return true
# 	def isEmployee(self):
# 		return True

# emp1 = Person("Noor") 
# print(emp1.getName())

# emp2 = Employee("Kallur") # no constructor specified, hence init of base will be called
# print(emp2.getName())

# # if you want to add an extra attribute to the instance like salary in the child class,  provide init and since a new self is created the attributes has to newly created for chilclass and parent attribute will be different unless it has the same name 
class Person:
    def __init__(self, name , color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def introduce_self(self):
        print("My name is " +self.name)
    
    def showColor(self):
        print("My color is " +self.color)
        
    def __str__(self):
        return f"Name:{self.name}, color:{self.color}, weight:{self.weight}"
    
    def __del__(self):
        print("Parent is being deleted "+self.name)


class Worker(Person):
    def __init__(self, name, color, weight, salary):
        self.cname = name # this cname attribute only belongs to base # self represents the current obj, so when "introduceself" is called the self makes sures the obj is of child not the parent
        self.color = color # this color attribute only belongs to base # since parent and child has the same attribute it we can access color from the parent
        self.weight = weight # this weight attribute only belongs to base
        self.salary = salary # this salary attribute belongs to only child
        
    def showSalary(self):
        return self.salary
    
    def __str__(self):
        return f"CName:{self.cname}, Ccolor:{self.color}, Cweight:{self.weight} Csalary{self.salary}"
    
    def __del__(self):
        print("Child is being deleted "+self.cname)

p1 = Person("Kallur", "blue", 45)
print(p1)
w1 = Worker("Noor", "red", 50, 100)
# w1.introduce_self() # it has access to parents class function, at this time self refers to child, throws error as self.name is not present in child
w1.showColor() # does not throw error as it has self.color too in parent class, at this time self refers to child and will return child color
print(w1)# if child does not have a __str func it will call parents __Str or else it will override and call the child __str


# # instead of creating new init for the same name color weight attributes use parent class init by using super keyword
#############################################################################################################################
# # SUPER keyword --> basically represents the parent class in child class
# #  https://blog.hubspot.com/website/python-super
# # Note : using super ignores the ambiguity in a diamond problem(expalined in the post, read for other advantages as well)
# class Person:
    
#     def __init__(self, name , color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
        
#     def introduce_self(self):
#         print("My name is " +self.name)
        
#     def __str__(self):
#         return f"Name:{self.name}, color:{self.color}, weight:{self.weight}"
    
#     def __del__(self):
#         print("Parent is being deleted "+self.name)


# class Worker(Person):
    
#     # def __init__(self, name, color, weight, salary): # developer way
#     #     base = super(Worker, self)
#     #     base.__init__(name, color, weight)
#     #     self.salary = salary
    
#     def __init__(self, name, color, weight, salary): # traditional way
#         # super(Worker, self).__init__(name, color, weight)
#         super().__init__(name, color, weight) # super() is same as super(Worker, self) 
#         self.salary = salary
    
#     def showSalary(self):
#         return salary
    
#     # def __str__(self): # traditional way
#     #     return f"CName:{self.name}, Ccolor:{self.color}, Cweight:{self.weight}, Csalary:{self.salary}"
    
#     def __str__(self): # noor way
#         base = super(Worker, self)
#         return f"{base.__str__()}, Csalary:{self.salary}"
    
#     def __del__(self):
#         print("Child is being deleted "+self.name)

# w1 = Worker("Noor", "red", 50, 1000)
# print(w1)
# print(w1.name)
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

