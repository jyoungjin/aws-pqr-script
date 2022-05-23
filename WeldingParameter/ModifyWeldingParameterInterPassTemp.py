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
                if "interpass_temp(°C)" in object:
                    temp = object["interpass_temp(°C)"]
                    temp = float(temp)
                    object["_interpass_temp(°C)"] = temp
                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')