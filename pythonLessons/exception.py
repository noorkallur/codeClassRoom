#https://www.w3schools.com/python/python_try_except.asp
try:
    age = int(input('Age: '))
    income = 10000
    risk = income / age
    #print(x) #the first error will trigger the exception blocks, error after it wont even be hit
    print(f"age - {age} risk - {risk}")
except ValueError:
    print("Invalid entry for age")
except ZeroDivisionError:
    print("Age cannot be 0")
except TypeError:
    print("Type error entry")
except:
    print(f"something else went wrong")
else:
    print(f"print when no errors are caught")
finally:
    print(f"printing regardless of try and except") 

print("yay")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") # raise own error from existing list of python errors