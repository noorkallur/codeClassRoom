def fibo(num):
    if num < 0:
        return
    if 0 == num:
        return 0
    if 1 == num:
        return 1
    return fibo(num -1) + fibo(num -2) #tail-recurison

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, .......
print(fibo(10))