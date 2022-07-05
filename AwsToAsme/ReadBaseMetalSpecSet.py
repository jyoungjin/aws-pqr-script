import json
import os

dir_path = "/Users/youngjin/workspace/json-data/aws-to-asme-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                if 'material_spec' in jsonData['base_metals'] and 'type_and_grade' in jsonData['base_metals']:

                    material_spec = jsonData['base_metals']['material_spec']
                    to_material_spec = jsonData['base_metals']['to_material_spec']
                    type_and_grade = jsonData['base_metals']['type_and_grade']
                    to_type_and_grade = jsonData['base_metals']['to_type_and_grade']

                    key = "spec: "+material_spec+", type:"+type_and_grade+""
                    to_key = "spec: "+to_material_spec+", type:"+to_type_and_grade+""
                    counts[key] = counts.get(key, 0) + 1
                    counts[to_key] = counts.get(to_key, 0) + 1

for item in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(item)

print(len(counts))
# for item in counts.keys():
#     print(item, end=', ')