def helperFun(substr, str, res):
    if len(str) == 0:
        if len(substr)!=0:
            res.append(substr)
        return
    helperFun(substr +  str[0], str[1:], res)
    helperFun(substr, str[1:], res)
    
def subsets(str):
    res = []
    substr = ""
    helperFun(substr, str, res)
    print(res)
    return res

str = "abc"
# str = "abcdef"
subsets(str)
    