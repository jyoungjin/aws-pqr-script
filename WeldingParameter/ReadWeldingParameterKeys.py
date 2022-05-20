import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            for object in jsonData['welding_parameters']:
                for key in object:
                    counts[key] = counts.get(key, 0)+1

for item in sorted(counts.items()):
    print(item)

print(len(counts))

# for item in counts.keys():
#     print(item, end=', ')