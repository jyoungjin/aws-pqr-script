import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()
allCnt = 0

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                allCnt += 1
                if 'welding_process1' in jsonData['pqr_info']:
                    key = jsonData['pqr_info']['welding_process1']
                if jsonData['pqr_info']['welding_process2'] is not None and jsonData['pqr_info']['welding_process2'] != '':
                    key += '+'
                    key += jsonData['pqr_info']['welding_process2']
                if jsonData['pqr_info']['welding_process3'] is not None and jsonData['pqr_info']['welding_process3'] != '':
                    key += '+'
                    key += jsonData['pqr_info']['welding_process3']
                counts[key] = counts.get(key, 0)+1

for item in counts.items():
    print(item)

print("총 파일수: ", allCnt)

# for item in counts.keys():
#     print(item, end=', ')