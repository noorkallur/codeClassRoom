def maxProfitNoor(prices):
    """_summary_
    DOESNOT work. Code failed
    """
    max = 0
    stack = []
    for price in prices:
        while len(stack) > 1:
            curr = price - stack[-1]
            if curr > max:
                max = curr
                stack.append(price)
            else:
                stack.pop()
 
        stack.append(price)
    
    return max 



def maxProfitDev(prices):
    minPrice = 10001
    maxDiff = 0
    
    for price in prices:
        # if price < minPrice:
        #     minPrice = price
        minPrice = min(minPrice, price) # simpler looking code but takes time to process as using internal methods
        # if maxDiff < price - minPrice:
        #     maxDiff = price - minPrice
        maxDiff = (maxDiff, price -minPrice) 
        
    return maxDiff



prices = [7,1,5,3,6,4]
print(maxProfitDev(prices))
        