# # info:https://replit.com/@codewithharry/91-Day-91-Generators-in-Python#.tutorial/Tutorial.md

# def simplegen():
#     yield 1
#     yield 2
#     yield 3
    
# print(next(simplegen())) #accessing the function so returns the first yield i.e. 1
# print(next(simplegen())) #accessing the function so returns the first yield i.e. 1

# iter = simplegen() #iter is a generator object which is iterable(it contains 1 ,2 ,3)

# print(next(iter)) #iterate to 1st yield
# print(next(iter)) #iterate to 2 yield
# print(next(iter)) #iterate to 3 yield

def dynamicGenerator():
    for i in range(5):
        yield i
       
gen = dynamicGenerator()#gen is a generator object which is iterable(it contains only "int" which is dynamically yiedls int val)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))