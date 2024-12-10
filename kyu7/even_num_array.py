def even_numbers(arr: list = None, n: int = None):
    even = [i for i in arr if i%2 == 0]
    return even[-n:]
            
