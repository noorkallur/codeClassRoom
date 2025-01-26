##for loops

# for element in 'python':
#     print(element)
# for item in ['noor', 'kallur', 'noor']:
#     print(item)
# for item in range(5, 10, 2):
#     print(item)

## total cost of items in the shopping cart
# cart_item_prices = [10, 20 ,30, 50]
# total = 0
# for item_price in cart_item_prices :
#     total += item_price
# print(f'Total cart value: {total}')

## nested for loops
# for x in range(4):
#     for y in range(3):
#         print(f"({x} , {y})")
     
# # When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# # To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))   # format determines which one index corresponds to what

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(a, q))   # here the format is changed
    
# # more on looping techinques https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

##challenge: print alaphabets in 'x' format
# alpha_nums = [5, 2, 5, 2, 2]
# for item in alpha_nums:
#      print('x' * item)

# alpha_nums = [5, 2, 5, 2, 2]
# for item in alpha_nums:
#     output=''
#     for xes in range(item):
#         output+='x'
#     print(output)

# while loops
prev_state = 0
while(1):
    user_inp=input('>').lower()
    if user_inp == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit 
        ''')
    elif user_inp == "start" and prev_state != 1:
        prev_state = 1
        print("car sarted ....")
    elif user_inp == "stop" and prev_state != 2:
        prev_state = 2
        print("car stopped")
    elif user_inp == "quit":
        print("exiting...")
        break
    else:
        if prev_state == 1:
            print("car is in motion already")
        if prev_state == 2:
            print("car in idle state already")
        print("enter valid input")
