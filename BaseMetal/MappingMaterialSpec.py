import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()

spec = sys.argv[1]
grade = sys.argv[2]
modify_spec = sys.argv[3]
modify_grade = sys.argv[4]
modify_group = sys.argv[5]

if len(sys.argv) != 6:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)

            if jsonData['base_metals']["material_spec"] == spec and jsonData['base_metals']["type_and_grade"] == grade:
                jsonData['base_metals']["_specification"] = modify_spec
                jsonData['base_metals']["_grade"] = modify_grade
                jsonData['base_metals']["_group"] = modify_group

            if jsonData['base_metals']["to_material_spec"] == spec and jsonData['base_metals']["to_type_and_grade"] == grade:
                jsonData['base_metals']["_to_specification"] = modify_spec
                jsonData['base_metals']["_to_grade"] = modify_grade
                jsonData['base_metals']["_to_group"] = modify_group

            with open(file_path, 'w', encoding='utf-8') as mk_f:
                json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)