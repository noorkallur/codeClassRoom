def product_of_digits(num):
    if num < 10:
        return num
    return num%10 * product_of_digits(num//10)  


print(product_of_digits(1342))
print(product_of_digits(10920))
print(product_of_digits(1))
print(product_of_digits(0))