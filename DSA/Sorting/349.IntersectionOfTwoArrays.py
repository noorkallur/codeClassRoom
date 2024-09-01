# https://leetcode.com/problems/intersection-of-two-arrays/description/
def IntersectionofTwoArrays(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    num1Point = 0
    num2Point = 0
    ans = []
    while num1Point < len(nums1) and num2Point < len(nums2):
        if nums1[num1Point] < nums2[num2Point]:
            num1Point +=1
        else:
            if nums1[num1Point] == nums2[num2Point]:
                if len(ans) != 0 and ans[-1] != nums1[num1Point]:
                    ans.append(nums1[num1Point])
                elif len(ans) == 0:
                    ans.append(nums1[num1Point])
                num1Point +=1
                num2Point +=1
            else:
                num2Point +=1
    return ans

nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(IntersectionofTwoArrays(nums1,  nums2))