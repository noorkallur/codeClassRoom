# class Robot:
#     def introduce_self(self): # have to add slef(this object) as postional argument otherwise def of that specific class wont work
#         print("My name is " +self.name)
# ## default constructor building object        
# r1 = Robot()
# # r1.introduce_self() #calling before attribute creation will cause an error
# r1.name = "Tom" # attribute can be added after the object is created
# r1.color = "red"        
# r1.weight = 120
# r1.introduce_self() 

# # classes with constructor(init) and destructor(del)
# class Robot2:
#     def __init__(self, name , color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
        
#     def introduce_self(self):
#         print("My name is " +self.name)
    
#     def __del__(self):
#         print("Robot2 is being deleted "+self.name)
        
        
# r2 = Robot2("Tom", "Red", "40Kgs")
# r3 = Robot2("Jerry", "blue", 6)
# r2.introduce_self()
# r3.introduce_self()

## __str__()
# # The __str__ method in Python is a special method that returns a string representation of an object. 
# # It is called when the built-in str() function is called on an object.
# class Robot2:
#     def __init__(self, name , color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
        
#     def introduce_self(self):
#         print("My name is " +self.name)
        
#     def __str__(self):
#         return f"Name:{self.name}, color:{self.color}, weight:{self.weight}"
    
#     def __del__(self):
#         print("Robot2 is being deleted "+self.name)
        
        
# r2 = Robot2("Tom", "Red", "40Kgs")
# r3 = Robot2("Jerry", "blue", 6)
# r2.introduce_self()
# r3.introduce_self()
# print(r2)

# # Class variables :: these are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. 
# # They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable
# class Robot2:
#     robot_total = 0
#     def __init__(self, name , color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         Robot2.robot_total +=1
        
#     def __del__(self):
#         print("Robot2 is being deleted "+self.name)
#         Robot2.robot_total -=1
        
    
# r2 = Robot2("Tom", "Red", "40Kgs")
# r3 = Robot2("Jerry", "blue", 6)
# print(Robot2.robot_total)

