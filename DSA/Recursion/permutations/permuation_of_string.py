# Permuations of a string "abc"
# permuations of this string means it has to all the chars in it. The possible solution "abc", "bac", "bca", "acb", "cab", "cba"
# Basically find permuations for three _3_ * _2_ * _1_ ==> 6 permuations

# how to go about this?
# we use the same principle as the subset recursion algorithm
# check the recursion diagram permutation_of_string.png
def permuations_string(str):
    res = []
    permStr = ""
    helperFun(str, permStr, res)
    return res

def helperFun(str, permStr, res):
    if len(str) == 0:
        res.append(permStr)
        return
    for i in range(len(permStr) + 1):
        # here comes the splicing and adding char in between the permuation string
        # divide in two parts acording  to the positon you want to place the char in 
        f = permStr[0:i]
        s = permStr[i:len(permStr)]
        # add char in between (directly passing in arg)
        print( f + str[0] + s)
        helperFun(str[1:], (f + str[0] + s) , res)
    
str = "abcd"
str = "abc"
ans = permuations_string(str)
print(ans)
print(len(ans))
