def add_sales (argv):
    programm, value = argv
    fp = open('bakery.csv', 'a', encoding = 'utf8')
    fp.writelines(value + '\n')
    fp.close()

if __name__ == '__main__':
    import sys
    exit(add_sales(sys.argv))