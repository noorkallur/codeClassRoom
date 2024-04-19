#################################################################################################################
# https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc
# Operator overloading and some magic methods
# magic methods has dunder(__)
# pre-requisites: other is a keyword which represents the same class object
class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __repr__(self): #means representation, if you dont have str dunder then this would be printed
        return f"rX:{self.x}, rY:{self.y}"
    
    def __str__(self):
        return f"X:{self.x}, Y:{self.y}"
    
    def __len__(self): # returns for len(object)
        return 100
    
    def __call__(self):
        return f"object is called"
        
v1 = Vector(2, 4)
v2 = Vector(5, 6)
v3 = v1 + v2 # operator overloading
print(v3) 
print(len(v3))
print(v2())