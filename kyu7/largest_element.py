def largest(n, xs):
    if n == 0:
        return []
    my_list = sorted(list(xs))
    return my_list[-n:]

            