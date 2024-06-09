def sum_of_digits(num):
    if num < 10:
        return num
    return num%10 + sum_of_digits(num//10)  


def sum_of_digits_2(num):
    if num == 0:
        return 0
    return num%10 + sum_of_digits_2(num//10)  


print(sum_of_digits(1342))
print(sum_of_digits(10920))
print(sum_of_digits(1))
print(sum_of_digits(0))
