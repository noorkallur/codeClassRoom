###############Method overloading###############################
## No support of Method overloading in python
# class Base():
    
#     def __init__(self, name, age):
#         print(f"Child3")
#         self._name = name
#         self._age = age
        
#     def method(self):
#         print("without args")
                
#     def method(self, one, two):
#         print("with args")
        
        
# c3 = Base("Noor", 26)
# # c3.method() #throws error
# c3.method(1,2)


###############Operator overloading###############################
# # docs.python : https://docs.python.org/3/reference/datamodel.html#special-method-names
# # list of operator overload examples: https://docs.python.org/3/reference/datamodel.html#emulating-container-types
class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y # default type is returned
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y) # casted to type class "Vector"
    
    def __str__(self):
        return f"X:{self.x}, Y:{self.y}"
    
    def __len__(self): # returns for len(object)
        return 100
    
    def __call__(self): # object calls syntax: <object>()
        print("object is called")
        
v1 = Vector(2, 4)
v2 = Vector(5, 6)
v3 = v1 + v2 # operator overloading
print(type(v3)) # tuple by default
v4 = v1 - v2 # operator overloading
print(type(v4)) # tuple by default
print(v4) 
print(len(v4))
v4()
        