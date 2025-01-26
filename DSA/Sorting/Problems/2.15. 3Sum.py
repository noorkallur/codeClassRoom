def threeSum(nums):
    nums.sort()
    res= []
    for i, negVal in enumerate(nums):
        if negVal > 0:
            break
        if i > 0 and nums[i-1]==negVal: # we already found all the possible solutions for number so go to next
            continue
        s = i+1
        e = len(nums)-1
        while s < e:
            threeSum = nums[s] + nums[e] + negVal
            if threeSum == 0:
                res.append([nums[i] , nums[s], nums[e]]) # found the answer why not break here? there could multiple answers for same neg number 
                s+=1                                   
                while nums[s] == nums[s-1] and s < e:   # go to next number if the current number is same as previos number(to prevent duplicate) and it should not cross end 
                    s+=1
            elif threeSum  > 0:
                e-=1
            else:
                s+=1
                
    return res
    
nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0,0]
print(threeSum(nums))

# https://www.youtube.com/watch?v=jzZsG8n2R9A