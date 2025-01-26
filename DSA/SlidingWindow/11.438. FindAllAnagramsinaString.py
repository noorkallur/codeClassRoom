def findAnagrams(s, p):
    hash_map_c = {}
    hash_map_p = {}
    for i in range(len(p)):
        hash_map_p[p[i]] = 1 + hash_map_p.get(p[i], 0)
        hash_map_c[s[i]] = 1 + hash_map_c.get(s[i], 0)
    output=[0] if hash_map_c == hash_map_p else []
    winStart = 0
    for winEnd in range(len(p), len(s)):
        hash_map_c[s[winEnd]] = 1 + hash_map_c.get(s[winEnd], 0)
        hash_map_c[s[winStart]]-=1
        if hash_map_c[s[winStart]] == 0:
            hash_map_c.pop(s[winStart])
        winStart +=1
        if hash_map_c == hash_map_p:
            output.append(winStart)
  
    return output

s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
# s = "abab"
# p = "aba"
print(findAnagrams(s, p))