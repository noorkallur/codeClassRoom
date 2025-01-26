l = [1, 4, 5, 7, 8]
# # MAP
cubeList = list(map(lambda x: x*x*x, l))
print(cubeList)
# # FILTER
filterList = list(filter(lambda x  : x>1, l))
print(filterList)
# # REDUCE
from functools import reduce
reduceVal = reduce(lambda x, y : x + y, l)
print(reduceVal)