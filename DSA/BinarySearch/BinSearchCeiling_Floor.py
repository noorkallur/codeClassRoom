# # cieling -> if target is not present then next value greater than the target shall be returned
# #  take a look at the code it returns start , start will be pointing to the ceiling value of the target
def ceilingOfArray(array, target):
    s = 0 
    e = len(array) - 1
    
    if(array[e] < target): # if my last value is less than target, return -1
        return -1
    
    while(s <= e):
        mid = int((s+e)/2)
        if(array[mid] == target):
            return mid
        if(array[mid] > target):
            e = mid - 1
        if(array[mid] < target ):
            s = mid + 1
    return s # as the start would be pointing to the next greater value of target at the end of iterations


array = [1, 2, 5, 6, 7, 9]
result = ceilingOfArray(array, 9)
print(f"Index -> {result} value ->{ array[result]}")


def floorOfArray(array, target):
    s = 0 
    e = len(array) - 1
    
    if(array[s] > target): # if first value is itself greater than target, return -1
        return -1
    
    while(s <= e):
        mid = int((s+e)/2)
        if(array[mid] == target):
            return mid
        if(array[mid] > target):
            e = mid - 1
        if(array[mid] < target ):
            s = mid + 1
    return e


array = [2, 2, 5, 6, 7, 9]
result = floorOfArray(array, 5)
print(f"Index -> {result} value ->{ array[result]}")