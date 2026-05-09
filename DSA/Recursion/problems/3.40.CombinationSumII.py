def combinator(target, index):
    if target == 0:
        res.append(sol[:])
        print(sol)
        return
    for i in range(index, len(candidates)):
        print(f"i:{i}, index:{index}, target:{target}, subtarget: {target - candidates[i]} sol:{sol}")
        if target - candidates[i] < 0:
            break
        if i > index and candidates[i] == candidates[i-1]:
            # before passing the next element check if its the same as before, note if the i is at beginging(index) dont check
            print(f" same i: {i} index: {index}")
            continue

        sol.append(candidates[i])
        combinator(target - candidates[i], i+1)
        sol.pop()


# start
candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
res = []
sol = []
combinator(target, 0)
print(res)