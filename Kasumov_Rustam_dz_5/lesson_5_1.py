def odd_nums(nums):
    for num in range(1, nums + 1):
        if num % 2 != 0:
            yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
for i in range(1, 15):
    print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
