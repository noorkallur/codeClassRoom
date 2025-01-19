# Find all the substring of the given string?
# the idea is to follow the logic of recursion but, iteratively thats why you see a kind of a tree(Please go thru the image susbstring_using_iteration.png)

# initial design by noor.
def subsets(str):
    res = []
    res.append("")
    res.append(str[0])  #something felt off becoz of this
    for i in range(1,len(str)):
        for j in range(len(res)):
            res.append(res[j]+str[i])
    print(res)
    
subsets("abc")

# better answer from another DEV. its just easy to understand and write
def subsets(str):
    res = [""]
    for char in str:
        res = res + [item + char for item in res]
    print(res)
    
subsets("abc")

# modified answer by noor for the previous. conclusion: should have thought about the initial empty string and adding to it iteratively
def subsets(str):
    res = []
    res.append("")
    for i in range(len(str)):
        for j in range(len(res)):
            res.append(res[j]+str[i])
    print(res)
    
subsets("abc")

