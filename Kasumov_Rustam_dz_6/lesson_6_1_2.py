log_list = []
log_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf8') as fp:
    line = fp.readline()
    while line:
        remote_add_r = line[0:(line.find('[')) - 5]
        request_type = line[line.find('"') + 1:line.find(' ', line.find('"'))]
        requested_resource = line[line.find('/dow'):line.find(' ', line.find('/dow'))]
        log_tuple = (remote_add_r, request_type, requested_resource)
        log_list.append(log_tuple)
        log_dict.setdefault(remote_add_r, 0)
        log_dict[remote_add_r] += 1
        line = fp.readline()
print(log_list)
sq = max(log_dict.values())
for key, val in log_dict.items():
    if val == sq:
        print(f'IP спамера --> {key} количество запросов {val}')
