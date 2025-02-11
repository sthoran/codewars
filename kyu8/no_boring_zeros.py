def no_boring_zeros(n):
    if n% 10 == 0 and len(str(n))>1:
        new_digit = str(n)
        return int(new_digit.rstrip('0'))
    return n