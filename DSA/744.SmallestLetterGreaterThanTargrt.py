# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def smallestLetterGreaterThanTarget(letters, target):
    s = 0
    e = len(letters)-1
    if letters[e] < target:
        return letters[s]
    while s<=e:
        mid = int((s+e)/2)
        if letters[mid] == target:
            s = mid +1
        elif letters[mid] > target:
            e = mid - 1
        elif letters[mid] < target:
            s = mid + 1
    return letters[s]

print(smallestLetterGreaterThanTarget(["a", "c", "c", "c", "d"], "c"))