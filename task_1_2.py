list_numb = []
for var in range(1, 1001, 2):
    list_numb.append(var ** 3)
sum_numb = 0
for var_two in list_numb:
    temp_sum = 0
    var_three = var_two
    while var_two != 0:
        temp_sum += var_two % 10
        var_two = var_two // 10
    if temp_sum % 7 == 0:
        sum_numb += var_three
for var in range(len(list_numb)):
    list_numb[var] += 17
print(sum_numb)
sum_numb = 0
for var_two in list_numb:
    temp_sum = 0
    var_three = var_two
    while var_two != 0:
        temp_sum += var_two % 10
        var_two = var_two // 10
    if temp_sum % 7 == 0:
        sum_numb += var_three
print(sum_numb)


