def merge(nums1, m, nums2, n):
    lPtr = 0
    rPtr = 0
    merged_array = []
    while lPtr < (m-n) and rPtr < n:
        if nums1[lPtr] < nums2[rPtr]:
            merged_array.append(nums1[lPtr])
            lPtr +=1
        else:
            merged_array.append(nums2[rPtr])
            rPtr +=1
    
    while lPtr < (m-n):
        merged_array.append(nums1[lPtr])
        lPtr +=1      
    
    while rPtr < n:
        merged_array.append(nums2[rPtr])
        rPtr +=1 
    
    for i in range(0, m):
        nums1[i] = merged_array[i]
        
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [3, 5, 6]
merge(nums1, 6, nums2, 3)
print(nums1)