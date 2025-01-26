def square_digits(num):
    res = 0
    while num != 0:
        dig = num%10
        res = (dig * dig) + res
        num = num//10
    return res


def isHappy(n):
    fastP = n
    slowP = n
    #using floyd's algo to find if the loop is present
    while True:
        slowP = square_digits(slowP)
        fastP = square_digits(square_digits(fastP))
        if fastP == 1 or slowP == 1: # pointers reached 1 
            return True
            
        if fastP == slowP: #loop is present
            return False
        

print(square_digits(square_digits(145)))
print(isHappy(19))
print(isHappy(2))