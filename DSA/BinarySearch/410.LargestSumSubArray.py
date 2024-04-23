from icecream import ic
def sum(arr):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

def getNoOfSubArrays(arr, mid):
    sum = 0
    subArrays = 1
    for num in arr:
        sum = sum + num
        if sum > mid:
            subArrays +=1
            sum = num
    return subArrays    

def largestSumSubArrayBinSearch(arr, maxSubArrays):
    
    if 1 == maxSubArrays:
        return sum(arr)
    
    arrlen = len(arr)
    if arrlen == maxSubArrays:
        return max(arr)

    s = max(arr)
    e = sum(arr)
    while(s < e):
        mid = (s + e) // 2
        noOfSubArrays = getNoOfSubArrays(arr, mid)
        if noOfSubArrays <= maxSubArrays:
            e = mid
        else:
            s = mid + 1
    return s


arr = [7, 5, 2, 8, 10]
# print(getSplits(arr, 18))
print(largestSumSubArrayBinSearch(arr, 2))
