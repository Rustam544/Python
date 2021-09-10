#  ВАРИАНТ № 1

time_text = ['дн', 'час', 'мин', 'сек']
time_result = []
time_deliver = [60, 60, 24]
remainder = 0
duration = int(input("Пожалуйста введите время:", ))
if duration < 1:
    print("Вы ввели неправильное значение!")
    exit()
for divider in time_deliver:
    remainder = duration % divider
    duration = duration // divider
    time_result.append(remainder)
time_result.append(duration)
time_result.reverse()
for idx in range(len(time_result)):
    if time_result[idx] > 0:
        print(time_result[idx], time_text[idx], end=' ')
print('\n')

def time_shift(res, tm, shift):
    if tm != 0:
        res = res + str(tm) + " " + shift + " "
    return res


# ВАРИАНТ № 2


time = int(input("Пожалуйста введите время:"))
day = time // (60 * 60 * 24)
hour = (time // (60 * 60)) % 24
mins = (time // 60) % 60
sek = time % 60
result = time_shift("", day, "дн")
result = time_shift(result, hour, "час")
result = time_shift(result, mins, "мин")
result = time_shift(result, sek, "сек")
print(result)
