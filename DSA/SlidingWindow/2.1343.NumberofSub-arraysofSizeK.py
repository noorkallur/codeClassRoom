# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

def numOfSubarrays(arr, k, threshold):
    curr_sum = 0
    count = 0
    winStart = 0
    for winEnd in range(len(arr)):
        curr_sum += arr[winEnd]
        if winEnd - winStart + 1 == k:
            if curr_sum / k >= threshold:
                count +=1  
            curr_sum -= arr[winStart] 
            winStart +=1
    
    return count

def numOfSubarrays(arr, k, threshold):
    total=sum(arr[:k])
    cnt=1 if total/k >=threshold else 0
    for i in range(k,len(arr)):
        total=total+arr[i]-arr[i-k]
        if total/k >= threshold:
            cnt+=1
    
    return cnt

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k , threshold))

