import os
import random

type_lists = []
dict_files = {100000: 0, 10000: 0, 1000: 0, 100: 0}
dict_types = {100000: set(), 10000: set(), 1000: set(), 100: set()}
dict_files_types = {}
file_sizes = [100, 1000, 10000, 100000]
path = os.path.join(os.getcwd(), 'my_project')
for root, dirs, files in os.walk(path):
    for file in files:
        with open(os.path.join(root, file), 'w', encoding='utf8') as f:
            for i in range(1, random.randint(1, 10 ** 5)):
                content = random.randint(0, 10)
                f.writelines(str(content))
            point_pos = file.find('.')
            fil_size = os.stat(os.path.join(root, file)).st_size
            for frz in file_sizes:
                if fil_size <= frz:
                    dict_files[frz] += 1
                    dict_types[frz].add(file[point_pos:])
                    break
for key in dict_files.keys():
    if dict_types[key] == set():
        dict_types[key] = None
    tuple_files = (dict_files[key], dict_types[key])
    dict_files_types[key] = tuple_files
print(dict_files_types)
