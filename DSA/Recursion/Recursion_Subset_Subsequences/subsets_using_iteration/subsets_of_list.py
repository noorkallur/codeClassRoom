def subsets(nums):
    # [] 1
    # [] 1, 2, 12
    # [] 1, 2, 12, 3, 13, 23, 123
    res = [[]]
    for num in nums:
        res = res + [item + [num] for item in res]
    return res
nums=[1, 2, 3]
print(subsets(nums))
    