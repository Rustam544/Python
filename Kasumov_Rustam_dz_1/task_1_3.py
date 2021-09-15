for i in range(1, 101):
    if 11 <= i <= 14:
        print(i, "Процентов")
    elif i % 10 == 1:
        print(i, "Процент")
    elif 1 < i % 10 < 5:
        print(i, "Процентa")
    else:
        print(i, "Процентов")
