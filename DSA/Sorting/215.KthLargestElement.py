# https://leetcode.com/problems/kth-largest-element-in-an-array/
def partition(arr, l, r): # look at the txt to understand intiution better
    """_summary_
    assumes the last element as pivot and shuffles it to the right place
    """
    pivot = arr[r]
    print(pivot)
    i = l
    
    for j in range(i,r):
        if arr[j]<pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
            
    arr[i], arr[r] = arr[r], arr[j]
    return i

def quick_slect(arr, l, r, k):
    low = l
    high = r
    piv_idx = partition(arr, low, high)
    print(arr)
    if piv_idx == k-1:
        return arr[piv_idx]
    elif piv_idx > k - 1:
        return quick_slect(arr, low, piv_idx-1, k)
    else:
        return quick_slect(arr, piv_idx+1, high, k)
    
arr = [1, 5, 3, 2, 4]
print(quick_slect(arr, 0, (len(arr)-1), 2))
print(arr)
        