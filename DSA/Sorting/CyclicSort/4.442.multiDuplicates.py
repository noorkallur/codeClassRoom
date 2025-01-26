def findMultiDuplicate(nums):
    def swap(i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
    i = 0
    while i < len(nums):
        correctIndex = nums[i] -1
        if nums[i] != nums[correctIndex]:
            swap(i, nums[i] -1)
        else:
            i+=1
    
    i = 0
    ans = list()
    while i < len(nums):
        if nums[i] != i+1:
            ans.append(nums[i])
        i+= 1
    return ans

nums = [4,3,2,7,8,2,3,1]

print(findMultiDuplicate(nums))