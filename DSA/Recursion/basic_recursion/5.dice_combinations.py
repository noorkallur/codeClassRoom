# how many combinations can num can be done throwing a dice

# for eg , 2 can have [1, 1], [2]

# for eg ,7
# 1, 1, 1, 1, 1, 1, 1
# 1, 1, 1, 1, 1, 2
# 1, 1, 1, 1, 3
# ...

def diceCombinations(target):
    result = []
    currSol = []
    def combinations(target):
        if target == 0:
            result.append(currSol[:])
            currSol.clear()
            return

        for i in range(1, target+1):
            subTarget = target - i
            if subTarget < 0:
                continue
            currSol.append(i)
            combinations(subTarget)
    
    combinations(target)
    return result
    
ans = diceCombinations(3)
ans = diceCombinations(4)
ans = diceCombinations(7)
print(ans)
# ans = diceCombinations(4)
# print(ans)
