def topKFrequentNoor(nums, k):
    """
        Does not work, misunderstood the question
    """
    ans = []
    hash_map = {}
    for num in nums:
        hash_map[num] = 1 + hash_map.get(num, 0)
    
    for key in hash_map:
        if k == 0:
            break
        ans.append(key)
        k -= 1
    
    return ans

# https://youtu.be/YPTqKIgVk-k
# https://leetcode.com/problems/top-k-frequent-elements/description/
def topKFrequent(nums, k):
    #create a list of list of frequencies    
    freq = []
    for i in range(len(nums) + 1):
        freq.append([])
    
    # hash map counter for each value    
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
    
    #update freq list with respect to freq, i.e if 1 and 3 appears twice then freq[2] = [1, 3]
    for key, val in counter.items():
        freq[val].append(key)
    print(freq)
    
    # go through the freqList backwards and append the entries to the answer till k is reached
    ans =[]
    for i in range(len(freq)-1, 0, -1):
        for key in freq[i]:
            ans.append(key)
        if len(ans) == k:
            return ans
    

nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
nums = [1, 2, 2]
k = 2
nums = [1, 2, 3, 1, 2]
k = 2
print(topKFrequent(nums, k))