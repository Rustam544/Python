src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
buffer = set()
for elem in src:
    if elem in buffer:
        buffer.remove(elem)
    else:
        buffer.add(elem)
for elem in src:
    if elem in buffer:
        result.append(elem)
print(result)
