# if matrix is sorted BOTH row and coloumn wise then we can sort from bottom logic
def searchIn2DArray(Matrix2DArray, target):
    r = 0
    c = len(Matrix2DArray) - 1
    
    while r < len(Matrix2DArray) and c >= 0:
        if Matrix2DArray[r][c] == target:
            return(r, c)
        if Matrix2DArray[r][c] > target:
            c -=1
        else:
            r +=1
    return (-1, -1)

mat2Darray = [
    [10 ,20, 30 ,40],
    [11 ,22, 35 ,46],
    [13 ,25, 37 ,49],
    [17 ,28, 39 ,50]
]
print(searchIn2DArray(mat2Darray, 50))