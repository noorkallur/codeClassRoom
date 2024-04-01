# # Binarysearch searches through sorted array, it cuts the array in half every time it doesnot find the element and hence it is called Binary search
def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        # mid = int(start + (end - start)/2) # no need
        mid = int((start + end)/2) # python3 has no max int limit hence mid = (start + end)/2 works
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1

array = [1, 2, 5, 6, 7, 9] 
# print(binarySearch(array, 10))

# # order agnostic BINARY SEARCH(dont know whether the input array is ascending or descending)
def agnosticBinarySearch(array, target):
    start = 0
    end = len(array) - 1
    if array[start] < array[end]: #ascending
        while start <= end:
            mid = int((start + end)/2) 
            if target == array[mid]:
                return mid
            elif array[mid] < target:
                start = mid + 1
            elif array[mid] > target:
                end = mid -1
        return -1
    elif array[start] > array[end]:# descending
        while start <= end:
            mid = int((start + end)/2) 
            if target == array[mid]:
                return mid
            elif array[mid] > target:
                start = mid + 1
            elif array[mid] < target:
                end = mid -1
        return -1
    else:
        print(f"All objects in array are equal")
        return start if array[start] == target else -1


array = [1, 2, 5, 6, 7, 9]
# print(agnosticBinarySearch(array, 5)) 
array = [10, 9, 6, 5, 3, 1]  
print(agnosticBinarySearch(array, 5)) 
array = [5, 5, 5, 5]  
# print(agnosticBinarySearch(array, 6)) 