def subsetsDuplicate(nums):
    # 1
    # 1, 2, 12
    # 1, 2, 12, 2, 12, 22, 122 avoid 2 ,12 again
    res = [[]]
    for num in nums:
        for i in range(len(res)):
            sublist = res[i] + [num]
            if not sublist in res:  # straight up checking if sublist are present in the res
                res += [sublist]
    return res

nums=[1, 2, 2]
ls = subsetsDuplicate(nums)
for l in ls:
    print(l)

# keeping track of index of the previous sublists,  to not to add dupicates 
def subsets(nums):
    # 1
    # 1, 2, 12
    # 1, 2, 12, 2, 12, 22, 122 avoid 2 ,12 again
    res = [[]]
    for i in range(len(nums)):
        s = 0
        if i != 0 and nums[i] == nums[i-1]: 
            s = e # previous end , in this case [1, 2, [1,2], 2] point the start at [1,2] which is previous end.. to avoid adding 2 to 1, 2 again
        e = len(res)
        for j in range(s, e): # using index to traverse
            sublist = res[j] + [nums[i]]
            res += [sublist]
    return res

nums=[1, 2, 2]
ls = subsets(nums)
for l in ls:
    print(l)