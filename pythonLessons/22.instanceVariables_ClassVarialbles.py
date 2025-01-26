# #lets see about class objects and how they can acess methods in a class
# class Employee:
#     def __init__(self, name):
#         self._name = name
    
#     def showDetails(self): #need object to be accessed
#         print(f"Emp name is {self._name}")
        
#     def OnlyClassCanCall(): #only accessed by class not objects
#         print(f"only class can call this with no obj")

# e1 = Employee("noor")

# e1.showDetails() # whenever we call a method of a class the class object is passed as argument i.e showDetails(e1) is passed
# Employee.showDetails(e1)  # is same as e1.showDetails() from above explanaiton

# # # e1.OnlyClassCanCall() # throws an error saying arg is passed
# Employee.OnlyClassCanCall() # Only calss can access but not the class objects 

# # CLASS variable
class Employee:
    
    Raise_amount = 0.05 #Class variable, this belongs to class but not objects and hence cannot be modified by class objects
    noOfEmployees = 0  
    
    def __init__(self, name):
        self._name = name
        Employee.noOfEmployees += 1
    
    def showDetails(self): #need object to be accessed
        print(f"Emp name is {self._name} and raise is {self.Raise_amount}")
        
e1 = Employee("Noor")
e1.Raise_amount = 0.10 # Here a new attribute called Raise_amount is created by object, called instance variable (this is not modifying calss variable Raise_amount )
print(e1.noOfEmployees)
e2 = Employee("Kallur")
e2.showDetails()


        