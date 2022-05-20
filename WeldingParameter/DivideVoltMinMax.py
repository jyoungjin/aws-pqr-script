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
                if 'volt(V)' in object:
                    value = object['volt(V)']
                    if "~" in value:
                        arr = value.split('~')
                        if float(arr[0]) > float(arr[1]):
                            print("앞에 수가 더 큽니다.")
                            print(jsonData['pqr_info']['procedure_qualification_record_no'])
                        object['volt_min(V)'] = float(arr[0])
                        object['volt_max(V)'] = float(arr[1])
                    else:
                        object['volt_min(V)'] = float(value)
                        object['volt_max(V)'] = float(value)

                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')