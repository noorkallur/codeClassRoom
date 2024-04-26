# https://leetcode.com/problems/fair-candy-swap/description/
# find the additonal value to add to each array
# aSum + bSum = total
# eqlCandy = total/2
# additional val to be added for aSum , call it d =  eqlCandy - aSum
# using algebra d in terms of aSum and aSum is d = (aSum - aSum)/2
# so from delta we know eqlCandyA + delta = eqlCandyB - dleta

def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        # mid = int(start + (end - start)/2) # no need
        mid = int((start + end)/2) # python3 has no max int limit hence mid = (start + end)/2 works
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1
# eqlCandyA + d = eqlCandyB - d
# find a value in "b" such that it is equal to (a[i] + d), swapping will subtract "d" from "b" and adds to "a"
def fairCandySwap(aliceSizes, bobSizes) :
    d = (sum(bobSizes) - sum(aliceSizes))/2
    bobSizes = sorted(bobSizes)
    for a in aliceSizes:
        bobSwapIndex = binarySearch(bobSizes, a+d)
        if -1 != bobSwapIndex:
            return [a, bobSizes[bobSwapIndex]]
    return -1


aliceBoxes = [1,1]
bobBoxes = [2,2]
aliceBoxes = [1, 1, 2, 4]
bobBoxes = [1, 2, 3, 4]
aliceBoxes = [2]
bobBoxes = [1,3]
aliceBoxes = [35,17,4,24,10]
bobBoxes = [63,21]
print(fairCandySwap(aliceBoxes, bobBoxes))