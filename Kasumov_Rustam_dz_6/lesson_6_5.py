def unity_files(argv):
    program, file1, file2, file3 = argv
    line = '0'
    fp = open(file1, 'r', encoding='utf8')
    fp2 = open(file2, 'r', encoding='utf8')
    fp3 = open(file3, 'w', encoding='utf8')
    while line:
        line = fp.readline().replace('\n', '')
        line2 = fp2.readline().replace('\n', '')
        if line2 == '':
            line2 = 'None'
        write_line = line + ': ' + line2 + '\n'
        if line:
            fp3.write(write_line)
            print(write_line)
    fp.close()
    fp2.close()
    fp3.close()


if __name__ == '__main__':
    import sys

    exit(unity_files(sys.argv))
