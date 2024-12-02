import string

def kyu8_is_uppercase(inp):
    special_char=string.punctuation
    for i in inp:
        if i in string.punctuation and i.isupper():
            return True
        if inp.isupper():
            return True
    else:
        return False
