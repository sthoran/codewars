import re
def hydrate(drink_string): 
    drinks = sum(map(int, re.findall('\d+', drink_string)))
    if drinks == 1:
        return f"{drinks} glass of water"
    return f"{drinks} glasses of water"