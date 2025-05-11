def countWays(target, coins):
    if target == 0:
        return 1
    
    count = 0
    for coin in coins:
        subTarget = target - coin
        if subTarget >= 0:
            count += countWays(subTarget, coins)

    return count

coins = [1, 4, 5]
print(countWays(5, coins))
# print(countWays(50, coins))

# memoize top down approach
def countWays(target, coins):
    memo = {}

    def recursive(target):
        if target == 0:
            return 1
        
        if target in memo:
            return memo[target]
        
        count = 0
        for coin in coins:
            subTarget = target - coin
            if subTarget >= 0:
                count += recursive(subTarget)

        memo[target] = count
        return count

    return recursive(target)

coins = [1, 4, 5]
print(countWays(5, coins))
print(countWays(50, coins))


# BOTTOM UP APPROACH with memoization
def countWays(target, coins):
    memo = {}
    memo[0] = 1 # if i reach one that means i got one way
    for val in range(1, target+1):
        for coin in coins:
            subtarget = val-coin
            if subtarget >= 0:
                memo[val] = memo.get(val, 0)+memo.get(subtarget)

    return memo[target]


coins = [1, 4, 5]
print(countWays(5, coins))
print(countWays(50, coins))
