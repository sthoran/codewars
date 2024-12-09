def catch_sign_change(lst):
    count = 0
    for idx, value in  enumerate(lst):
        if idx == 0:
            pass
        elif value < 0 and lst[idx-1] >= 0:
            count += 1
        elif value >= 0 and lst[idx-1] < 0:
            count += 1
    return count