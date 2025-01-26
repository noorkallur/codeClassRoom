# # Consider a module to be the same as a code library.
# # A file containing a set of functions you want to include in your application.
# # https://www.w3schools.com/python/python_modules.asp
import module1 # use the module we just created, by using the import statement
from  module1 import greeting
from  module2 import greeting# can import only parts of module
from  module2 import whereami# can import only parts of module
from datetime import datetime
greeting("Noor") # When using a function from a module, use the syntax: module_name.function_name.

print(greeting.__doc__) # prints the doc string

whereami()

print(datetime.now())

y = max(5, 10, 25)
x = abs(-7.25)
print(x)
print(y)

print(dir(module1)) # prints all the defns in that module