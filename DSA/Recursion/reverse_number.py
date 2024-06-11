def reverse_number_1(num):
    if num == 0:
        return 0
    units = 1
    localNum = num
    while localNum >=10:
        units *= 10
        localNum = localNum//10
    return (num%10)*units + reverse_number_1(num//10)

print(reverse_number_1(1234))


def base_mltpler(num):
    if num == 0:
        return 1
    return 10 * base_mltpler(num//10)


def reverse_number_2(num):
    if num == 0:
        return 0
    return (num%10)*base_mltpler(num) + reverse_number_2(num//10)

print(reverse_number_2(1234))