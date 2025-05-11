# with out memoization
def minCoins(target, coins):
    def min_none(a, b):
        if a == None:
            return b
        if b == None:
            return a
        return min(a,b)
    
    def recursive(target):
        if target == 0:
            return 0
        
        cur_ans = None
        for coin in coins:
            subTarget = target-coin
            if subTarget < 0:
                continue
            cur_ans = min_none(cur_ans, recursive(subTarget) +1)
        return cur_ans

    return recursive(target)


coins =[5, 4, 1]
print(minCoins(13, coins))

# another way without the memoization
def minCoins(target, coins):
    ans = float('inf')
    def recursive(target, cnt):
        nonlocal ans
        if target == 0:
            ans = min(ans, cnt)
            return
        
        for coin in coins:
            subTarget = target-coin
            if subTarget < 0:
                continue
            
            recursive(subTarget, cnt+1)
         

    recursive(target, 0)
    return ans


coins =[5, 4, 1]
print(minCoins(13, coins))

# memoization
def minCoins(target, coins):    
    memo = {}
    def recursive(target):

        if target == 0:
            return 0
        if target in memo:
            return memo[target]
        cur_ans = float('inf')
        for coin in coins:
            subTarget = target-coin
            if subTarget >= 0:
                cur_ans = min(cur_ans, recursive(subTarget) +1)

        memo[target] = cur_ans
        return cur_ans

    return recursive(target)


coins =[5, 4, 1]
print(minCoins(13, coins))

coins =[5, 4, 1]
print(minCoins(150, coins)) 