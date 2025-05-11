mem = {}
def fib(n):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1
    
    res = fib(n-1) + fib(n-2)
    mem[n] = res
    return res

print(fib(5))
print(fib(50))

def fib(n):
    mem = {}

    for i in range(1 ,n+1):
        if i<=2:
            res = 1
        else:
            res = mem[i-1] + mem[i-2]
        
        mem[i] = res
    
    return mem[n]

print(fib(5))
print(fib(50))
