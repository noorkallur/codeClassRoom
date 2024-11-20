# from sortedcontainers import SortedList
    # sorted_window = SortedList()
def getSubarrayBeauty(nums, k, x):
    def getSmallestInteger(x):
        for i in range(-50, 0):
            x -=hash_map[i]
            if x < 0:
                print(i)
                return i
        
        return 0 
                
    hash_map = {i:0 for i in range(-50, 51)}
    winStart = 0
    min_array = []
    for winEnd in range(len(nums)):
        hash_map[nums[winEnd]] = 1 + hash_map.get(nums[winEnd], 0)
        if sum(hash_map.values()) == k:
            min_array.append(getSmallestInteger(x))
            hash_map[nums[winStart]] -= 1
            winStart +=1        
    
    return min_array
        
nums = [-1,-2,-3,-4,-5]
k = 2
x = 2
nums = [1,-1,-3,-2,3]
k = 3
x = 2
nums = [-3,1,2,-3,0,-3]
k = 2
x = 1
nums = [-46,-34,-46]
k =3
x =3
nums = [2,-22,2]
k =2
x =3
nums = [2,-22,2]
k =2
x =3
nums = [-14,9,13,-26,47,-39,-49,-14,29]
k =9
x =4
print(getSubarrayBeauty(nums, k, x))