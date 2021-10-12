import json

user_list = []
hobby_list = []
dict_hobby = {}
with open('users.csv', 'r', encoding='utf8') as fp:
    line = fp.readline().replace('\n', '')
    while line:
        user_list.append(line)
        line = fp.readline().replace('\n', '')

with open('hobby.csv', 'r', encoding='utf8') as fp:
    line = fp.readline().replace('\n', '')
    while line:
        hobby_list.append(line)
        line = fp.readline().replace('\n', '')


if len(user_list) < len(hobby_list):
    print('1')
else:
    with open('users_hobby.csv', 'w', encoding='utf8') as fp:
        for i in range(len(user_list)):
            if i >= len(hobby_list):
                hobby_list.append(None)
            dict_hobby.setdefault(user_list[i], hobby_list[i])
        json.dump(dict_hobby, fp)
    with open('users_hobby.csv', 'r', encoding='utf8') as fp:
        print(json.load(fp))
