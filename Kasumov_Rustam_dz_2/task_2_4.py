prof_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for variable in range(len(prof_name)):
    message = prof_name[variable][:prof_name[variable].rfind(' '):-1]
    print('Привет, ' + message[::-1].title() + '!')
