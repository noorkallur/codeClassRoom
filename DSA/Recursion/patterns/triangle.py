def triangle_from_base(row, col):
    if row == 0:
        return
    if col < row:
        print("*", end=" ")
        triangle_from_base(row, col+1)
    else:
        print("")
        triangle_from_base(row-1, 0)
    
triangle_from_base(4, 0)

def triangle_from_head(row, col):
    if row == 0:
        return
    if col < row:
        triangle_from_head(row, col+1)
        print("*", end=" ")
    else:
        triangle_from_head(row-1, 0)
        print("")
    
triangle_from_head(4, 0)
        
        
