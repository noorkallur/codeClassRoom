def fourSum(nums, target):
    nums.sort()
    res= []
    for num1idx, num1 in enumerate(nums):
        if num1idx > 0 and nums[num1idx-1]==num1:  # we already found all the possible solutions for number so go to next
            continue
        for num2idx in range(num1idx+1, len(nums)):
            if num2idx > num1idx+1 and nums[num2idx-1] == nums[num2idx]: # we already found all the possible solutions for the second number so go to next
                continue
            s = num2idx+1
            e = len(nums)-1
            while s < e:
                fourSum = nums[s] + nums[e] + nums[num2idx] + num1
                if fourSum == target:
                    res.append([nums[num1idx], nums[num2idx] , nums[s], nums[e]]) # found the answer why not break here? there could multiple answers for same neg number 
                    s+=1                                   
                    while nums[s] == nums[s-1] and s < e:   # go to next number if the current number is same as previos number(to prevent duplicate) and it should not cross end 
                        s+=1
                elif fourSum  > target:
                    e-=1
                else:
                    s+=1
                
    return res

nums = [1,0,-1,0,-2,2]
target = 0
# nums = [2,2,2,2,2]
# target = 8
print(fourSum(nums, target))