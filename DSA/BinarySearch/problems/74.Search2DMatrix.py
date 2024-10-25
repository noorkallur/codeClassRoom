def search2DMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    end = rows * cols -1
    
    while start <= end:
        mid = (start + end) // 2
        row =  mid // cols # divide by cols to know the row
        col = mid % cols # the remainder is the col 
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1 
    
    return False 


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34   
print(search2DMatrix(matrix, target))         
        
    