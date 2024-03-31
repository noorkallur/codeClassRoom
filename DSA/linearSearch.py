# Linear search traverse through each elements
nums = [ 2, 4, 7, 2, 7, 9, 5]
def linearSearch(nums, target):
    for num in nums:
        if num == target:
            return nums.index(num)
# print(linearSearch(nums, 7))

#Minimum number in array
def minimumNumber(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
# print(minimumNumber(nums))

#search in 2d array
Array2D = [
    [4, 2, 8],
    [2, 9, 12],
    [34, 9346, 457]
]
#index based search, traditional way
def searchIn2Darray(array, target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if target == array[i][j]:
                return [i , j]
    return -1
# print(searchIn2Darray(Array2D, 12))

#python for loops and finding the index in the end
def searchIn2DarrayPythonway(array, target):
    for row in array:
        for col in row:
            if target == col:
                return [array.index(row), row.index(col)]
    return -1
print(searchIn2DarrayPythonway(Array2D, 12))