def sum_of_zeros_noor(num):
    if num == 0:
        return 0
    if num%10 == 0:
        sum =  1
    else:
        sum = 0
    return sum + sum_of_zeros_noor(num//10)  

print(sum_of_zeros_noor(1352057))
print(sum_of_zeros_noor(0))
print(sum_of_zeros_noor(100001))



def sum_of_zeros(num):
    return helper_sum_of_zeros(num, 0)

def helper_sum_of_zeros(num, sum):
    if num == 0:
        return sum
    if num%10 == 0:
        sum += 1
    return helper_sum_of_zeros(num//10, sum)  


print(sum_of_zeros(1352057))
print(sum_of_zeros(0))
print(sum_of_zeros(100001))