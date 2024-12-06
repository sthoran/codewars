def expected_value(r: int, c: int) -> int:
    
    sum_j = c * (c + 1) // 2
    total_sum =  (c + 1) * r * (r + 1) // 2 - (r + 1) * sum_j
    numb_elements = (r + 1) * (c + 1)

    return int(total_sum // numb_elements)

    
 
      