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
            if 'size_of_electrode' in jsonData['filler_metals']:
                size_of_electrode = jsonData['filler_metals']["size_of_electrode"]
                if type(size_of_electrode) == dict:
                    print("aa")
                    jsonData['filler_metals']["_size_of_electrode(mm)"] = {}
                    for key in size_of_electrode.keys():
                        jsonData['filler_metals']["_size_of_electrode(mm)"][key] = jsonData['filler_metals']["size_of_electrode"][key].lower().strip("mm")
                else:
                    jsonData['filler_metals']["_size_of_electrode(mm)"] = jsonData['filler_metals']["size_of_electrode"].lower().strip("mm")
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')