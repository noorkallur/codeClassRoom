def checkInclusion(s1, s2):
    hash_map_s1 = {}
    for ch in s1:
        hash_map_s1[ch] = 1 + hash_map_s1.get(ch, 0)

    hash_map_s2 = {}
    winStart = 0
    for winEnd in range(len(s2)):       
        hash_map_s2[s2[winEnd]] = 1 + hash_map_s2.get(s2[winEnd], 0)
        if sum(hash_map_s2.values()) >= sum(hash_map_s1.values()):
            if hash_map_s2 == hash_map_s1:
                return True
            else:
                hash_map_s2[s2[winStart]] -= 1
                if hash_map_s2[s2[winStart]] == 0:
                    hash_map_s2.pop(s2[winStart])
                winStart +=1
             
    return False

s1 = "aba"
s2 = "eidbaaooo"
s1 = "ab"
s2 = "eidboaoo"
s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))