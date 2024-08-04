# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
def twoSum(numbers, target):
    s = 0
    e = len(numbers)-1
    
    while s < e:
        if numbers[s] + numbers[e] == target:
            return [s+1, e+1]
        elif numbers[s] + numbers[e] > target:
            e-=1
        else:
            s+=1
    return None

numbers = [2,7,11,15]
target = 9
numbers = [-1,0]
target = -1
numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))