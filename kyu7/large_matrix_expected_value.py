#matrix = [[1,2,3,4],[5,6,7,8],[1,2,3,4]]

def expected_value(r:int,c:int) -> int:
    matrix= [[j + i and i -1 for j in range(0, c)]
             for i in range(r )]
    
    #for i in range(r):
        #row= []
        #for j in range(c):
        #    row.append(i+1, j-1)
        #matrix.append(row)    
        
    return matrix    