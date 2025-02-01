def sq_sum_digits(num):
    sq_sum = 0
    while num:
        sq_sum += (num%10)**2
        num = num//10

    return sq_sum

def isHappy(num):
    slow = num
    fast = num
    
    while fast != 1:
        slow = sq_sum_digits(slow)
        fast = sq_sum_digits(sq_sum_digits(fast))
        
        if fast == slow:
            return False
    
    return True

n = 2
print(isHappy(n))

