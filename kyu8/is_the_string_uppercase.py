import string

def kyu8_is_uppercase(inp):
    special_char=string.punctuation
    #for i in inp:
    if inp.isupper():
        return True
    elif all(i in string.punctuation for i in inp):
        return True
    elif any(i.isdigit() for i in inp):
        return False
    else:
        return False