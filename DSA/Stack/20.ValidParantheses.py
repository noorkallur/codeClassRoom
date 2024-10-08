# https://leetcode.com/problems/valid-parentheses/description/
def isValidNoor(s:str) -> bool:
    stk =[]
    
    for char in s:
        
        if stk and char == ')':
            if stk.pop() != '(':
                return False
        elif stk and char == '}':
            if stk.pop() != '{':
                return False
        elif stk and char == ']':
            if stk.pop()!= '[':
                return False  
        else:    
            stk.append(char)
            
    if len(stk) == 0:    
        return True
    else:
        return False
            
s = "()"
print(isValidNoor(s))
s = "()[]{}"
print(isValidNoor(s))
s = "(]"
print(isValidNoor(s))
s = "([])"
print(isValidNoor(s))
s = "["
print(isValidNoor(s))
s = "}"
print(isValidNoor(s))

def isValidDev(s:str) -> bool:
    stk =[]
    close_to_open_dict ={
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s:
        if char in close_to_open_dict:
            if not stk:
                return False
            if stk.pop() != close_to_open_dict[char]:
                return False
        else:    
            stk.append(char)
    if stk:
        return False
    else:
        return True
            
s = "()"
print(isValidDev(s))
s = "()[]{}"
print(isValidDev(s))
s = "(]"
print(isValidDev(s))
s = "([])"
print(isValidDev(s))
s = "["
print(isValidDev(s))
s = "}"
print(isValidDev(s))