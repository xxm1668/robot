import json
import random

filename = r'/Users/haojingkun/PycharmProjects/robot/example/estate_qa.json'
outputs = []
data = []
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        json_data = json.loads(line)
        history = json_data['history']
        if len(history) > 0:
            continue
        if json_data not in data:
            data.append(json_data)
data = random.sample(data, 200)
for d in data:
    instruction = d['instruction']
    output = d['output']
    print('    - ' + instruction)
