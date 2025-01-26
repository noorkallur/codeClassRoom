def numberOfSteps(num):
    steps = 0
    return helper_fun(num, steps)
    
def helper_fun(num, steps):
    if num<=0:
        return steps
    if num%2 == 0:
        return  helper_fun(num//2, steps+1)
    else:
        return helper_fun(num - 1, steps+1)
    
print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))
print(numberOfSteps(0))
print(numberOfSteps(-1))