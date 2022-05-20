import json
import os

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                if 'specification' in jsonData['filler_metals'] and 'classification' in jsonData['filler_metals'] and 'f_no' in jsonData['filler_metals']:

                    specification = jsonData['filler_metals']['specification']
                    classification = jsonData['filler_metals']['classification']
                    f_no = jsonData['filler_metals']['f_no']

                    if type(specification) != dict:
                        key = specification + " " + classification + " " + f_no
                        counts[key] = counts.get(key, 0)+1


for item in counts.items():
    print(item)

print(len(counts))
# for item in counts.keys():
#     print(item, end=', ')