# def printNums(num):
#     if num == 0:
#         return
#
#     print(num) prints the num and then calls for recursion
#     printNums(num - 1)
    
# printNums(5)

# # Tail recursion:
# The above example is for tail recursion as the recursive funciton is the last one called

# # Non-Tail recursion: operation after the recursive function is called
# # #want to print from 1 to n
# def printNumsFromBegining(num):
#     if 0 == num: # break condition
#         return
    
#     printNumsFromBegining(num-1) #calls for recursion and when it returns we call the next line
#     print(num)
    
# printNumsFromBegining(5)

#want to print from  n to 1 and 1 to N
def printNums_N_to_1_to_N(num):
    if 0 == num: # break condition
        return
    
    print(num)
    printNums_N_to_1_to_N(num-1) 
    print(num)
    
printNums_N_to_1_to_N(5)