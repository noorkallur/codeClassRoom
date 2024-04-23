class parent1:
    def __init__(self) -> None:
        print("parent1")
    
    def showParentName(self):
        print("Parent 1")

class parent2:
    def __init__(self) -> None:
        print("parent2")

    def showParentName(self):
        print("Parent 2")

class child(parent2, parent1): # parent1 and parent2 order  matters while inheriting
    
    def __init__(self, name, age):
        print(f"Child")
        self._name = name
        self._age = age
        
c = child("Noor", 26)
print(child.mro()) # mro(method resoultion order) gives us the order of the inheritance
c.showParentName() # first it checks the "child" then parent class in the order of inheritance 
