def is_vow(inp):
    dict = {
        97: 'a', 101:'e', 105 : 'i', 111: 'o', 117 : 'u'}
    for number in inp:
        print(number)
        for k, v in dict.items():
            if k in number:
                print(number)