# # https://www.geeksforgeeks.org/python-property-function/
class NormalClass:
    def __init__(self, val) :
        self._value = val
    
    def showValue(self): #instead of this(getter) we can create a property decorator
        return self._value
    # # its is common pratice to have same "def value" for all the properties as its more inituitive although you could change the def names but its not better
    @property
    def value(self):
        print(f"entered property(getter)")
        return self._value 

    @value.setter
    def value(self, setVal):
        print(f"entered setter")
        self._value = setVal
    
    @value.deleter
    def value(self):
        print(f"entered deleter but not actually doing anything")
        pass #notice i have not actually deleted the value here , which goes to say propery only triggers the function but the implentaion shall be written by users 
    
obj = NormalClass(10)
# print(obj.showValue())
# print(obj.value) # this also does the same job print(obj._value)  but the important thing is @property provides encapsulation
# print(obj.ten_value)
obj.value #.value triggers propery(getter) of value
obj.value = 10  # "value = " triggers setter property of "value"
del obj.value # del key word triggers delete propery of "value"
