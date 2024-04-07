def binarySearchIndexBased(array, target, indxStart, indxEnd):
    start = indxStart
    end = indxEnd
    while start <= end:
        mid = int((start + end)/2) 
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1
# suppose array is infinite, hence not using len()
def inifinteArraySearch(array, target):
    s = 0
    e = s + 1
    try:
        while 1:
            if array[e] < target:
                s = e
                e = e * 2
            else:
                return binarySearchIndexBased(array, target, s, e)
    except IndexError:
        f"size of array{s*2 - 1} target {target} not found"
        return -1
    
    
array = []
for i in range(0, 1000):
    array.append((i + 1)*10)    
print(array)

print(inifinteArraySearch(array, 520))