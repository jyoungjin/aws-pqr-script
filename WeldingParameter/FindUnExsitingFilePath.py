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
                if "speed(mm/min)" not in object and "speed(cm/min)" not in object and "speed(in/min)" not in object and "action" not in object:
                    print(jsonData['pqr_info']['company'])
                    counts[jsonData['pqr_info']['procedure_qualification_record_no']] = counts.get(jsonData['pqr_info']['procedure_qualification_record_no'], 0)+1
                    break

for item in counts.items():
    print(item)

print(len(counts))

# for item in counts.keys():
#     print(item, end=', ')