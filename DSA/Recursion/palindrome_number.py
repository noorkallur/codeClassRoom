def reverse_number(num):
    if num == 0:
        return 0
    units = 1
    localNum = num
    while localNum >=10:
        units *= 10
        localNum = localNum//10
    return (num%10)*units + reverse_number(num//10)

def IsPalindrome(num):
    if num == reverse_number(num):
        return True
    else:
        False