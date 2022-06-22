import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()

# spec = sys.argv[1]
# grade = sys.argv[2]
# modify_spec = sys.argv[3]
# modify_grade = sys.argv[4]
# modify_group = sys.argv[5]
#
# if len(sys.argv) != 6:
#     print("Insufficient arguments")
#     sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)

            if type(jsonData['filler_metals']["_specification"]) != dict and type(jsonData['filler_metals']["_classification"]) != dict:
                if jsonData['filler_metals']["_specification"] == "AWS A5.17" and jsonData['filler_metals']["_classification"] == "SF7A(P)8-EH14":
                    jsonData['filler_metals']["_specification"] = "A 5.17"
                    jsonData['filler_metals']["_classification"] = "EH14"
                    jsonData['filler_metals']["_group"] = "II"
                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
