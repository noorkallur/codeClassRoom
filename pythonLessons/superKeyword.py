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
    
#     # def __init__(self, name, color, weight, salary): 
#     #     base = super(Worker, self) # example usage of super
#     #     base.__init__(name, color, weight)
#     #     self.salary = salary
    
#     def __init__(self, name, color, weight, salary): 
#         # super(Worker, self).__init__(name, color, weight) #old usage of super
#         super().__init__(name, color, weight) # super() is same as super(Worker, self)  # new usage of super
#         self.salary = salary
    
#     def showSalary(self):
#         return self.salary
    
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

###### Diamond problem###################################################################
class Person:
    
    def __init__(self, name, age):
        print(f"Person")
        self._name = name
        self._age = age
        
    def somethin(self):
        return 1
    
    def baseClassFUnc(self):
        print("baseclassFUnc")       
        
class child1(Person):
    
    def __init__(self, name, age):
        print(f"Child1")
        super().__init__(name, age)
        self._name = name
        self._age = age

    def somethin(self):
        return 2

class child2(Person):
    
    def __init__(self, name, age):
        print(f"Child2")
        super().__init__(name, age)
        self._name = name
        self._age = age

    def somethin(self):
        return 3
        
class child3(child2, child1): # child2 and child1 postion matters while inheriting
    
    def __init__(self, name, age):
        print(f"Child3")
        super().__init__(name, age)
        self._name = name
        self._age = age
        
c3 = child3("Noor", 26)
print(c3.somethin())
c3.baseClassFUnc()