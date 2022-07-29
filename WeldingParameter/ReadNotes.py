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
            for str in jsonData['notes']:
                newStr = str[3:len(str)]
                counts[newStr] = counts.get(newStr, 0)+1

for item in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(item)

print(len(counts))