# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# https://youtu.be/9ByWqPzfXDU?si=Ac5-2IfjXR3b_NSX&t=109
# Noor did this using similar logic as subsets using recursion
def letterCombinations(digits: str):
    if len(digits) == 0:
        return [] 
    hash_map = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
    
    def permuations(digits, ps, res):
        if len(digits) == 0:
            print(f"finalnode:{ps}")
            res.append(ps)
            return 
        us = hash_map[digits[0]]
        # add one char to ps 
        print(f"entering the iteration for us:{us}")
        for j in range(0, len(us)):
            print(f"entering j iteration {us[j]}")
            print(f"ps: {ps+us[j]}")
            permuations(digits[1:], ps+us[j], res)
    
    ps = ""
    res = []
    permuations(digits, ps, res) 
    return res  

lc = "23"
print(letterCombinations(lc))
                

       