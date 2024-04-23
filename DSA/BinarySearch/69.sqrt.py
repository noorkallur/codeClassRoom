# https://leetcode.com/problems/sqrtx/
def mySqrt(x):
    s = 1
    e = x
    while(s<=e):
        mid = (s + e)//2
        if mid*mid == x:
            return mid
        if mid * mid > x:
            e = mid - 1
        else:
            s = mid + 1
    return e

print(mySqrt(625))