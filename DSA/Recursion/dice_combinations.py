# how many combinations can num can be done throwing a dice
# for eg , 2 can have [1, 1], [2]

def diceCombinations(target):
    def combinations(p, up, res):
        if up == 0:
            res.append(p)
            return
        
        for num in range(1, up+1):
            # p.append(num) 
            # combinations(p, up - num, res) # here p is modified, so it will mess up recursive calls
            combinations(p + [num], up - num, res) # tip: inorder to preserve the p value at recursive calls dont modify in between directly send it in args
            
    res = []
    p = []
    combinations(p, target, res)
    return res
    
ans = diceCombinations(3)
ans = diceCombinations(4)
ans = diceCombinations(2)
print(ans)
# ans = diceCombinations(4)
# print(ans)
