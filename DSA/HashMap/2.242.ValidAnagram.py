# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter


def isAnagram(s, t) -> bool:
    if sorted(s) == sorted(t):
        return True
    else:
        return False
    
 
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
 
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# sorted does support unicode(ie all the characters not just ASCII) sorting
# Unicode character list https://symbl.cc/en/unicode-table/

