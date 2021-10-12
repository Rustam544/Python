from time import perf_counter

#  Option 1
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

start = perf_counter()

for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])

print(result, perf_counter() - start)

#  Option 2
result = []
start = perf_counter()


def max_list_add(num_list):
    for i in range(1, num_list):
        if src[i] > src[i - 1]:
            yield src[i]


result = max_list_add(len(src))
print(*result, perf_counter() - start)
