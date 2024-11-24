# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
def longestSemiRepetitiveSubstring(str):
    s = 0
    e = 1
    rep_p = 0
    rep  = False
    longest = 1
    while e < len(str):
        if str[e] == str[e-1] and rep == True:
            s = rep_p 
            rep_p = e
        elif str[e] == str[e-1] and rep == False:
            rep = True
            rep_p = e
        longest = max(longest, e-s+1)
        e +=1

    return longest

str = "5494" # res = 4
str = "52233" # res = 4
str = "1111111" # res = 2
str = "223533222"# res = 6
str = "0001" # res = 3
print(longestSemiRepetitiveSubstring(str))