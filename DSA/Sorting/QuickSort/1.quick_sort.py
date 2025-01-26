def swap(i , j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
    
def quick_sort(nums, low, high):
    if low>= high:
        return
    s = low
    e = high
    m = (s+e)//2
    piv = nums[m]
    
    #shuffle till the mid is at the right position
    while s <=e:
        while nums[s] < piv: # finding the left large element
            s +=1
        while nums[e] > piv: # finding the right small element
            e -=1
        
        if s<=e: # after every parse for finding elements make sure s and e does not cross each other
            swap(s, e, nums)
            s +=1
            e -=1
    quick_sort(nums, low, e)
    quick_sort(nums, s, high)
    

arr = [5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr)-1)
print(arr)