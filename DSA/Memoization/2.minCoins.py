# # with out memoization
# def minCoins(target, coins):
#     def min_none(a, b):
#         if a == None:
#             return b
#         if b == None:
#             return a
#         return min(a,b)
    
#     def recursive(target):
#         if target == 0:
#             return 0
        
#         cur_ans = None
#         for coin in coins:
#             subTarget = target-coin
#             if subTarget < 0:
#                 continue
#             cur_ans = min_none(cur_ans, recursive(subTarget) +1)
#         return cur_ans

#     return recursive(target)


# coins =[5, 4, 1]
# print(minCoins(13, coins))

# # another way without the memoization
# def minCoins(target, coins):
#     ans = float('inf')
#     def recursive(target, cnt):
#         nonlocal ans
#         if target == 0:
#             ans = min(ans, cnt)
#             return
        
#         for coin in coins:
#             subTarget = target-coin
#             if subTarget < 0:
#                 continue
            
#             recursive(subTarget, cnt+1)
         

#     recursive(target, 0)
#     return ans


# coins =[5, 4, 1]
# print(minCoins(13, coins))

# # memoization
# def minCoins(target, coins):    
#     memo = {}
#     def recursive(target):

#         if target == 0:
#             return 0
#         if target in memo:
#             return memo[target]
#         cur_ans = float('inf')
#         for coin in coins:
#             subTarget = target-coin
#             if subTarget >= 0:
#                 cur_ans = min(cur_ans, recursive(subTarget) +1)

#         memo[target] = cur_ans
#         return cur_ans

#     return recursive(target)


# coins =[5, 4, 1]
# print(minCoins(13, coins))

# coins =[5, 4, 1]
# print(minCoins(150, coins)) 


# Bottom Up
def minCoins(target, coins):
    # Initialize DP array with infinity for all values except 0
    cacheWays = [float('inf')] * (target + 1)
    cacheWays[0] = 0  # Base case: 0 coins needed to make amount 0

    # Build up the solution iteratively
    for amount in range(1, target + 1):
        for coin in coins:
            if amount - coin >= 0:
                # find the least ways possible
                cacheWays[amount] = min(cacheWays[amount], cacheWays[amount - coin] + 1)

    print(cacheWays)
    return cacheWays[target] if cacheWays[target] != float('inf') else -1

coins = [1, 2, 5]
print(minCoins(4, coins))
print(minCoins(1, coins))
print(minCoins(3, coins))