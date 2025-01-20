def norm_index_test(seq, ind): 
    if len(seq) == 0:
        return None
    return seq[ind%len(seq)]

        
