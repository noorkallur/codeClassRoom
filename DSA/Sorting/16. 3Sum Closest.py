def threeSumClosest(nums, target):
    nums.sort()
    
    ans = float('inf')
    for i, a in enumerate(nums):
        s = i + 1
        e = len(nums)-1
        while s < e:
            CurrSum = a + nums[s] + nums[e]

            if abs(target - CurrSum) < abs(target -ans):
                ans = CurrSum 
                
            if CurrSum > target:
                e-=1
            else:
                s+=1
                
    return ans       

nums = [-1,2,1,-4]
target = 1
nums = [1,1,1,0]
target = -100
print(threeSumClosest(nums, target))