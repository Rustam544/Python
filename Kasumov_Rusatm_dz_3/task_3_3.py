def thesaurus(*args):
    dict_args = {}
    key_str = ''
    for i in range(len(args)):
        if args[i][0] not in key_str:
            key_str += args[i][0]
    for i2 in key_str:
        list_name = []
        for i3 in range(len(args)):
            if i2 == args[i3][0]:
                list_name.append(args[i3])
        dict_args[i2] = list_name
    print(dict_args)


thesaurus("Иван", "Мария", "Петр", "Илья")
