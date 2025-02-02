# could not find the solution, its a stupid problem
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
def minInsertions(s):
    left = []
    right = []
    
    for br in s:
        if br == "(":
            left.append(")")
            left.append(")")
        elif not left and br == ")":
            if br == right[-1]:
                right.pop()
            else:
                right.append("(")
                right.append(")")
        else:
            left.pop()
            
    return len(left) + len(right)


            
s = "))())("
# s = "())"
# s = "(()))"
# s = ")))))))"
s = "(()))(()))()())))"
s = "(()))()))"
print(minInsertions(s))