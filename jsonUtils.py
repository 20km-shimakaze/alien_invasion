import json


def read_json(src):
    f = open(src, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return json.loads(content)


def write_json(src, data):
    now_mem = json.dumps(data, ensure_ascii=False)
    f = open(src, 'w+', encoding='utf-8')
    f.write(now_mem)
    f.close()


# print(read_json('data.json'))
# data = read_json('data.json')
# data['history'].append({'time': time.localtime(), 'score': 10})
# write_json('data.json', data)
# print(read_json('data.json'))
