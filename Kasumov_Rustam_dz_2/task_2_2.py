list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
cond_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
list_two = []
a = ''
for cond_list_two in list:
    if cond_list_two[0] in cond_list:
        list_two.append("\"")
        if cond_list_two[0] == '+': a = '+'
        if cond_list_two[0] == '-': a = '-'
        cond_list_two = f'{(abs(int(cond_list_two))):02d}'
        cond_list_two = a + cond_list_two
        a = ""
        list_two.append(cond_list_two)
        list_two.append("\"")
    else:
        list_two.append(cond_list_two)
print(list_two)
i =0
message = ''
while i < len(list_two):
    if list_two[i] == '\"':
        message += list_two[i] + list_two[i+1] + list_two[i+2] + ' '
        i += 3
    else:
        message += list_two[i]+' '
        i += 1

print(message)
