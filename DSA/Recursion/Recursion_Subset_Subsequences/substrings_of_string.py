# Find all the substrings of string using recursion?

# the best way to do this is adding and not adding char to substring recursively. I know you its hard to understand by words,
# refer the image(substrings_of_string.png) to understand better

def helperFun(substr, str, res):
    if len(str) == 0:
        if len(substr)!=0:
            res.append(substr) # we are appending all the substrings
        return
    helperFun(substr +  str[0], str[1:], res) # add the char to the substring, point to next char in the string
    helperFun(substr, str[1:], res) # donot add and char to substr, just point to next char in the string
    
def subsets(str):
    res = []
    substr = ""
    helperFun(substr, str, res) # helper function to pass the substring and also the output storage
    print(res)
    return res

str = "abc"
# str = "abcdef"
subsets(str)
    