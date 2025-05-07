# checkout the md file

def subsets1(nums):
    res = []
    sol = []
    def backtrack(i):
        if i == len(nums):
            res.append(sol[:])
            return
        
        # add
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

        # dont add
        backtrack(i+1)
        
    backtrack(0)
    return res

nums = [1, 2, 3] # order doesnot matter
res = subsets1(nums)

for r in res:
    print(r)


def subsets2(nums):
    res = []
    sol = []
    def backtrack(idx):
        res.append(sol[:])

        for i in range(idx, len(nums)):
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
    backtrack(0)
    return res

nums = [1, 2, 3] # order doesnot matter
res = subsets2(nums)

for r in res:
    print(r)

