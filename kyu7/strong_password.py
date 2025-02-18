def check_password(s):
    special_char= '!@#$%^&*?'
    not_included_special = '[_()<->/\|}+{~:]=;'
    rules = [lambda s: 8 <= len(s) <= 20 ,
             lambda s: any((char).isdigit() for char in s),
             lambda s: any((char).islower() for char in s),
             lambda s: any((char).isupper() for char in s),
             lambda s: any(char in s for char in special_char),
             lambda s: all(char not in s for char in not_included_special)]
    
    if all(rule(s) for rule in rules):
         return 'valid'
    else:
        return 'not valid'
         

    
    