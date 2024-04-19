# Info about them are present the url below
# https://replit.com/@codewithharry/71-Day-71-dir-dict-and-help-methods#.tutorial/Tutorial.md
class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
        
    def doSomething(self):
        """does something
        """
        self._age = self._age - 1
        
        
    def __str__(self):
        return f"THIS IS {self._name} object"
    
    
p = Person("Noor", 26)
# print(Person.__dict__) # lists features of class including attributes, methods
# print(p.__dict__) # lists all the  attributes assigned to the object
# print(p) # returns __str__
# print(help(Person)) # list all the info about that class
# print(help(p)) # list all the info about that class
print(p.doSomething.__dict__) # displays "{}"
