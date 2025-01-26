def findMedianSortedArrays(nums1, nums2):
    left = 0
    right = 0
    merged_arr = []
    while left < len(nums1) and right < len(nums2):
        if nums1[left] < nums2[right]:
            merged_arr.append(nums1[left])
            left +=1
        else:
            merged_arr.append(nums2[right])
            right+=1
    
    while left < len(nums1):
        merged_arr.append(nums1[left])
        left +=1
        
    while right < len(nums2):
        merged_arr.append(nums2[right])
        right +=1
    
    mer_len = len(merged_arr)
    print(merged_arr)
    if mer_len%2 == 0:
        return((merged_arr[mer_len//2 - 1] + merged_arr[mer_len//2])/2)
    else:
        return(merged_arr[mer_len//2])

    
nums1 = [1,3]
nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
nums1 = [1]
nums2 = [3]
print(findMedianSortedArrays(nums1, nums2))
 