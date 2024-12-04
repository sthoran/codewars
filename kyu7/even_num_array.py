def even_numbers(arr,n):
    even = [i for i in arr if i%2 == 0]
    return even[-n:]
            
