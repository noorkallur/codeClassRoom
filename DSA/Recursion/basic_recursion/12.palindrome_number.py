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

# rewrote the function
#is number a palindrome
# reverse a number and check if its the same
def reverseNumber(num, units):
    if num <= 0:
        return 0
    
    return (num%10 * units) + reverseNumber(num//10, units//10)
    
def isPalindrome(num):
    # count the units
    units = 1
    c_num = num
    while c_num>9:
        c_num = c_num//10
        units *=10

    if num == reverseNumber(num, units):
        return True
    else:
        return False


print(isPalindrome(123))
print(isPalindrome(1221))