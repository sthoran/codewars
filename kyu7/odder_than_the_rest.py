def odd_one(arr):
    for idx, i in enumerate(arr):
        if i %2 != 0:
            return idx
    return -1