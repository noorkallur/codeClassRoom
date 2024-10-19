# https://leetcode.com/problems/group-anagrams/description/

# figuring out how to group anagrams in the list
# sort the each element by alphabet so eat, tea, ate all become aet, so our key -value  aet : [ eat, tea, ate]

from collections import defaultdict


def groupAnagrams(strs):
    anagram_dict = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))
        anagram_dict[key].append(word)
    
    return list(anagram_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))