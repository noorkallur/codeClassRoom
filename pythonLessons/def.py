# # positional argument where the order of the postion matters
# def greet_user(name, place):
#     print(f"Hello {name}")
#     print(f"Welcome to the {place} quest")
# print("Your jounery starts here ! ")
# greet_user(input("whats your name wanderer > "), input("where do you want to go > "))
# print("Lets begin your adventure...")

# # key word arguments 
# def total_profit(revenue, operating_cost, discount):
#     print(f"Total profit is : {revenue - operating_cost - discount}")
# total_profit(operating_cost= 100, discount= 20, revenue= 500) # position doesnt matter and its mostly used for redability
# # total_profit(revenue= 600, operating_cost= 76.8)# throws error missing argument
# # total_profit(revenue= 600, operating_cost= 76.8, 0)# throws error postional arg is after the key word arg
# total_profit( 600,  discount= 0, operating_cost= 76.8,)# throws no error

# # *args and **kwargs in func parameters
# def myFun(arg1, arg2, arg3):
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Noor", "--", "Kallur") # these are positional
# myFun(*args)

# kwargs = {"arg3": "Kallur", "arg2": "--", "arg1": "Noor"} # keyword is mapped to the arg
# myFun(**kwargs)

# # assignment swear word censor
# swear_words= {
#     "hell" : "H***",
#     "shit" : "💩"
# }
# def swear_word_censor(input_message):
#     words = input_message.split(" ")
#     output = ""
#     for word in words:
#         output += swear_words.get(word, word) + " "
#     return output
# message = input("Enter your message here > ")
# print(swear_word_censor(message))

# # https://www.geeksforgeeks.org/first-class-functions-python/?ref=lbp
# # Functions can return another function 
# def create_adder(x): 
# 	def adder(y): 
# 		return x+y 
# 	return adder 
# add_15 = create_adder(15)  # use break point to see how it flows
# print(add_15(10)) #adder will return now as add_15 now has adder which was returned by create_adder, better understand https://www.geeksforgeeks.org/python-closures/?ref=lbp

# # Function decorators
# # https://www.youtube.com/watch?v=MYAEv3JoenI
# #  https://www.youtube.com/watch?v=PTBZ674EsvI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=59

# def greetFunction(func):
#     def wrapper(passedName):
#         print("Hello")
#         func(passedName)
#     return wrapper

# # @greetFunction
# def welcomFunction(name):
#     print(f"Welcome {name}")

# w = greetFunction(welcomFunction)

# w("noor")

# #function decorator without any args
# def someDecorator(func):
#     print(f"decorationg")
#     return func
# @someDecorator
# def someFunction():
#     print(f"this is a test")
# someFunction()

# #function decorator with any args
# def logging_call(func):
#     def decorated_func(*args, **kwargs): # args -> arguments, kwargs -> keyword args : refer above
#         print(f"logging: {func.__name__} with args = {args} and kwargs {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"returned {result}")
#         return func
#     return decorated_func
# @logging_call # if not @ for decorators use logging_call(add)(3, 5) to call
# def add(a , b):
#     return a + b
# add(3 ,5) #call decorator and passes func as an arg to that decorator

# another example for decorators time calculator decorator
# import time
# import math
# # decorator to calculate duration taken by a function
# def calculate_time(func):
# 	def wrapper(*args, **kwargs):
# 		begin = time.time()
# 		func(*args, **kwargs) #calling the function passed
# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)
# 	return wrapper
# @calculate_time
# def factorial(num):
# 	# sleep 2 seconds because it takes very less time
# 	# so that you can see the actual difference
# 	time.sleep(2)
# 	print(math.factorial(num))
# # calling the function.
# factorial(10)

