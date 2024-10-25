# https://leetcode.com/problems/koko-eating-bananas/description/
def minEatingSpeed(piles, h):
    def canEat(bnas):
        hrs_taken = 0
        for x in piles:
            rem = x/bnas
            rem = int(rem) + (rem % 1 > 0)
            hrs_taken = hrs_taken + rem 
            if hrs_taken > h:
                return False
        return True
    
    piles.sort()
    start = piles[0]
    end = piles[-1]
    min = 0
    
    while start <= end:
        mid = (start + end)//2
    
        if True == canEat(mid):
            min = mid
            end = mid -1
        else:
            start = mid + 1
            
    return min

#uses floor binary search
def minEatingSpeedDEv(piles, h):
    def eat_hrs(bnas):
        hrs = 0
        for pile in piles:
            hrs += (pile + mid - 1) // mid  # Equivalent to ceil(pile / mid)
        return hrs
    
    start = 1
    end = max(piles)
    
    while start < end:
        mid = (start + end)//2
    
        if eat_hrs(mid) <= h:
            end = mid
        else:
            start = mid + 1
            
    return end
    
piles = [3,6,7,11]
h = 8
piles = [30,11,23,4,20]
h = 5
# print(canEat(3, piles, h))
print(minEatingSpeed(piles, h))
