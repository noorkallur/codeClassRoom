def characterReplacement(s, k):
    hash_map={}
    winStart = 0
    maxsub = 0
    
    for winEnd in range(len(s)):
        hash_map[s[winEnd]]  = 1 + hash_map.get(s[winEnd], 0)
        while (winEnd - winStart + 1) - max(hash_map.values()) > k:
            hash_map[s[winStart]] -=1
            winStart += 1
            
        maxsub = max(maxsub, sum(hash_map.values())) 
        
    return maxsub

s = "ABAB"
k = 2
s = "AABABBA"
k = 1
print(characterReplacement(s, k))