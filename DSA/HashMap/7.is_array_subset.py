def is_array_subset(a, b):
    if len(a) > len(b):
        return is_array_subset(b, a)
    hm = {}
    for i in range(len(b)):
        hm[b[i]] = 1 + hm.get(b[i], 0)

    print(hm)

    for j in range(len(a)):
        if not hm.get(a[j], False):
            return False
        
    return True

a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

print(is_array_subset(a, b))

