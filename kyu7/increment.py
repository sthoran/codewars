def incrementer(nums):
    l =[]
    for i, idx in enumerate(nums):
        if i+(idx+1) > 9:
            l.append(int(str(i+(idx+1))[1]))
        else:
            l.append(i+(idx+1))
        
    return l
        
     
            
    