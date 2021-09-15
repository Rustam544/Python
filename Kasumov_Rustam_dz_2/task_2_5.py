original_list = [66.8, 94.1, 88.5, 57.3, 24.87, 90, 34.6, 23.89, 43.1, 54, 78.5, 98.4, 77, 12.54, 37.04]
price_list = original_list.copy()
print(id(price_list))
price_list.sort()
print(id(price_list))


def print_list(money):
    rub = int(money)
    cop = int(round(money - rub, 2) * 100)
    print(rub, "руб", f'{cop:02d}', "коп", end=", ")


for cash in price_list:
    print_list(cash)
print()
rev_price_list = reversed(price_list)
for cash in rev_price_list:
    print_list(cash)
print()

original_list.sort()
max_price_list = original_list[::-1][0:5]
print(max_price_list)
