import math as m
x_global = 5 # global var

def greeting(name):
  """ greets function by the name provided
  """
  print("module2, " + name)

def startGame():
    pass

def printVar():
  global x_global # to access/modify use global keyword
  x_global = 3

if __name__ == "__main__":
  print(x_global) # pritns 5
  printVar()
  print(x_global) # prints 3
      
def whereami():
    print(f"in Module2")

if __name__ == "__main__": # only run if the current module is main, used to avoid running calls when imported by other modules
  print(m.pi)