def show_sales(argv):
    program, *args = argv
    fp = open('bakery.csv', 'r', encoding='utf8')
    i = 0
    if args:
        if args[0]:
            while i <= int(args[0])-1:
                line = fp.readline().replace('\n', '')
                i += 1
            else:
                print(line)
    else:
        line = fp.readline().replace('\n', '')
        print(line)
    while line:
        if len(args) >= 2:
            if args[1]:
                i = int(args[0])
                if i <= int(args[1]):
                    i += 1
                    line = fp.readline().replace('\n', '')
                    print(line)
            fp.close()
            exit()
        line = fp.readline().replace('\n', '')
        print(line)
    fp.close()
    return


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))
