import numpy as np

def expected_value(r:int,c:int) -> int:
    matrix= [[i -j for j in range(c +1)]
             for i in range(r + 1 )]
    sum_element = np.sum(matrix)
    if r == 0:
        numb_elements = (r)*(c+1)
        return int(sum_element)
    else:
        numb_elements = (r+1)*(c+1)
    return int(sum_element/numb_elements)    
        
      