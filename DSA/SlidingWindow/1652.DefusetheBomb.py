def decrypt(code, k):
    if k == 0:
       return [0] * len(code)
    sub_sum = 0
    out_put = []
    iter = 0
    if k > 0:
        e = k
        s = e - k + 1
    else:
        s = abs(k)
        e = abs(k) + 1
    print(f"s:{s} e:{e}")
    sub_sum = sum(code[s:e+1])
    out_put.append(sub_sum)
    e = (e + 1)%len(code)
    print(f"s:{s} e:{e}")
    while iter < len(code)-1:
        sub_sum +=code[e]
        sub_sum -=code[s]
        out_put.append(sub_sum)
        s = (s + 1)%len(code)
        e = (e + 1)%len(code)
        print(f"s:{s} e:{e}")
        iter += 1
    
    return out_put


def decrypt(code, k):
    if k == 0:
       return [0] * len(code)
    out_put = [0] * len(code)
    sub_sum = 0
    if k > 0:
        # e = k
        # s = e - k + 1
        pass
    else:
        s = abs(k)
        e = abs(k) + 1
    print(f"s:{s} e:{e}")
    sub_sum = sum(code[s:e+1])
    out_put.append(sub_sum)
    e = (e + 1)%len(code)
    print(f"s:{s} e:{e}")
    while iter < len(code)-1:
        sub_sum +=code[e]
        sub_sum -=code[s]
        out_put.append(sub_sum)
        s = (s + 1)%len(code)
        e = (e + 1)%len(code)
        print(f"s:{s} e:{e}")
        iter += 1
    
    return out_put

code = [2,4,9,3]
k = -2
# code = [5,7,1,4]
# k = 3
# code = [5,7,1,4]
# k = 1
print(decrypt(code, k))
 