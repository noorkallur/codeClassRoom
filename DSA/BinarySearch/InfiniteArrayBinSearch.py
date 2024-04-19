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
    """Assuming the array is infinite, divide the search ranges starting from 1 and double it till we find the target in range
    """
    s = 0
    e = 1
    while 1:
        if array[e] < target:
            s = e + 1 # new start = prevend + 1
            e = e * 2 # new end = prevend*2
        else:
            return binarySearchIndexBased(array, target, s, e)
array = []
for i in range(0, 1000):
    array.append((i + 1)*10)    
print(array)

print(inifinteArraySearch(array, 520))