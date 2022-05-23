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
            if 'diameter' in jsonData['base_metals']:
                diameter = jsonData['base_metals']["diameter"].upper().strip("MM").strip("N/A")
                if diameter == "":
                    jsonData['base_metals']["_diameter(mm)"] = None
                else:
                    jsonData['base_metals']["_diameter(mm)"] = float(diameter)
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')