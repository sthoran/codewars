import re
def is_it_a_num(s: str) -> str:
    number = re.sub('\D','',s)
    for i in number:
        if int(i[0])==0 and len(number)==11:
            return number
    return "Not a phone number"
    