def lengthOfLongestSubstring(string):
    hash_set = set()
    winStart = 0
    max_sub_len = 0
    for winEnd in range(len(string)):

        while string[winEnd] in hash_set:
            hash_set.remove(string[winStart])
            winStart +=1
            
        hash_set.add(string[winEnd])
        max_sub_len = max(len(hash_set), max_sub_len)
    
    return max_sub_len
    

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "biidygcc"

print(lengthOfLongestSubstring(s))