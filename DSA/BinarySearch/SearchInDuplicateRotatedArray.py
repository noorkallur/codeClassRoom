def pivotIndexDuplicateRotatedArray(arr):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s+e)//2
        if mid < e and arr[mid] > arr[mid+1]:
            return mid
        if mid > s and arr[mid] < arr[mid-1]:
            return mid-1
        
        if arr[s] == arr[mid] and arr[mid] == arr[e]: # dupicate case where our prev logic wont work
            #check if start is pivot
            if arr[s] > arr[s+1]:
                return s
            s += 1 #skipping the duplicate
            #check if end is pivot
            if arr[e] > arr [e-1]:
                return e
            e += 1 #skipping the duplicate
            
        if arr[s] < arr[mid] or arr[s]==arr[mid] and arr[mid] > arr[e] :
            s = mid +1
        else:
            e = mid -1
    return -1

def pivotIndexDuplicateRotatedArray(nums):
    s = 0
    e = len(nums) -1
    
    while s <= e:
        mid = (s+e)//2   
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        if mid != 0 and nums[mid] < nums[mid - 1]:
            return mid
        
        if nums[mid] == nums[s] == nums[len(nums) -1]: # trimming if s == last == mid
            if nums[mid] != nums[e]:
                s = mid + 1
            else:
                s  += 1
                e  -= 1
            continue
        
        if nums[mid] > nums[len(nums) -1]:
            s = mid + 1
        else:
            e = mid - 1
    return - 1

print(pivotIndexDuplicateRotatedArray([9, 9, 9, 1, 2, 9, 9, 9, 9, 9]))#2
print(pivotIndexDuplicateRotatedArray([10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8])) #3
print(pivotIndexDuplicateRotatedArray([1, 2, 3, 4, 5, 6, 7, 8])) #-1
print(pivotIndexDuplicateRotatedArray([1, 2]))#-1
print(pivotIndexDuplicateRotatedArray([2, 1]))#0
print(pivotIndexDuplicateRotatedArray([2, 1]))#0
print(pivotIndexDuplicateRotatedArray([2,9,2,2,2]))#1
