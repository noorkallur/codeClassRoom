from collections import defaultdict


def twoSumNoor(nums, target):
    hash_map = defaultdict(int)
    for key, value in enumerate(nums):
        hash_map[value]= key
        
    for i, element in enumerate(nums):
        sec_index = hash_map[target - element]
        if sec_index != 0 and sec_index != i:
            return [i, sec_index]

 
nums = [3,3]
target = 6   
print(twoSumNoor(nums, target))

def twoSumDev(nums, target):
    hash_map ={}
        
    for i, element in enumerate(nums):
        delta = target - element
        if delta in hash_map:
            return [i, hash_map[delta]]
        hash_map[element] = i

 
nums = [3,3]
target = 6   
print(twoSumDev(nums, target))