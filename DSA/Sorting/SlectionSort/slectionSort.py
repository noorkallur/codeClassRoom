def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def selectionSort(nums):
    length = len(nums)
    for i in range(0, length - 1): #starts at 0 and ends at len-1(wont go in the loop)
        largest = 0
        for j in range(1, length -i): # j = 1 , to check prev element
            if nums[j] > nums[largest]:
                largest = j
            swap(largest, length -1 -i, nums)
        
arr = [5, 4, 3, 2, 1]
selectionSort(arr)
print(arr)

def UpdatedSelectionSort(nums):
    length = len(nums)
    for i in range(0, length - 1): #starts at 0 and ends at len-1(wont go in the loop)
        largest = 0
        for j in range(1, length -i): # j = 1 , to check prev element
            if nums[j] > nums[largest]:
                largest = j
        if largest != length -1 -i: #if the largest is at the right index dont swap
            swap(largest, length -1 -i, nums)
        
arr = [5, 4, 3, 2, 1]
selectionSort(arr)
print(arr)

#comparing j to the next element
def AnotherSelectionSort(nums):
    length = len(nums)
    for i in range(0, length - 1):
        largest = 0
        for j in range(0, length -i-1): # j = 0 , to check next element
            if nums[j+1] > nums[largest]:
                largest = j+1
        if largest != length -1 -i:
            swap(largest, length -1 -i, nums)
        
arr = [5, 4, 3, 2, 1]
AnotherSelectionSort(arr)
print(arr)