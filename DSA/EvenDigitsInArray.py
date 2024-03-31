def numOfDigits(num):
    digits = 0 
    while(num > 0) :
        digits += 1
        num = int(num/10)
    return digits

def findNumbers(nums):
    evenCount = 0
    for num in nums:
        digits = numOfDigits(num)
        if(digits%2 == 0):
            evenCount += 1
    return evenCount
print(findNumbers([12, 34, 567, 7, 89211, 67])            )