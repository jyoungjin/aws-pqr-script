import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()
find_key = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            for object in jsonData['welding_parameters']:
                for key in object:
                    if key == find_key:
                        counts[jsonData['pqr_info']['company']+jsonData['pqr_info']['procedure_qualification_record_no']] = counts.get(key, 0)+1

for item in counts.items():
    print(item)

print(len(counts))

# for item in counts.keys():
#     print(item, end=', ')