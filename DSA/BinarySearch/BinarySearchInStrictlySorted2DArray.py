def rowOfTarget(array, target):
    """return the row of the target
    searching in only first coloumn to know the row
    floor value logic to find the targets row index
    """
    firstColoumn = 0
    s = 0 
    e = len(array) - 1
    
    if(array[s][firstColoumn] > target): # if first value is itself greater return -1
        return -1
    
    while(s <= e):
        mid = int((s+e)/2)
        if(array[mid][firstColoumn] == target):
            return mid
        if(array[mid][firstColoumn] > target):
            e = mid - 1
        if(array[mid][firstColoumn] < target ):
            s = mid + 1
    return e

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

def searchInStrictSortedArray(mat2Darray, target):
    rowIndex = rowOfTarget(mat2Darray, target)
    if -1 != rowIndex:
        colIndex = binarySearch(mat2Darray[rowIndex], target)
    else:
        return (-1, -1)
    return (rowIndex, colIndex)

mat2Darray = [
    [1, 2, 3, 4],
    [21, 22, 23, 24],
    [31, 32, 33, 34],
    [41, 42, 43, 44]
]

print(searchInStrictSortedArray(mat2Darray, 21))