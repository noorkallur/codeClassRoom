# # No access modifiers in python, but a common practice among devs
class Employee:
    def __init__(self, name, id):
        self._name = name
        self.__id = id # sort of like protected
    
e = Employee("Noor", 1768)
print(e._name)  # python doesnt do anything regarding restricting access, but its a common convention to assume as protected by devs
# print(e.__id) # throws error : e object does not have any e.__id as that would be hidden from other attributes(kind of like private)
# you could access it using name mangling, as in python when you use double under for attribute it would be save as "_<className>__<attributeName>"(verify by running dir(e))
e._Employee__id = 3 # will work
print(e._Employee__id) # accessed indirectly by using name mangling