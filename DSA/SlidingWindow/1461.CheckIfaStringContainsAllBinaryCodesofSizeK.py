# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
def hasAllCodes(s, k):
    curr_sub = s[0:k]
    hash_set = set()
    hash_set.add(curr_sub)
    print(hash_set)
    for winEnd in range(k-1, len(s)):
        curr_sub = s[winEnd:winEnd+k]
        print(curr_sub)
        if len(curr_sub) == k:
            hash_set.add(curr_sub)
        print(hash_set)
        if len(hash_set) == k**2:
            return True
    return False

def hasAllCodes(s, k):
    if len(s) < k:
        return False
    
    hash_set = set()
    for i in range(len(s) - k + 1):
        curr_sub = s[i:i + k]
        hash_set.add(curr_sub)
    
    return len(hash_set) == 2 ** k





s = "01"
k = 1

s = "00110110"
k = 2
s = "0110"
k = 2
s = "0110"
k = 1
print(hasAllCodes(s, k))