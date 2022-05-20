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
                if 'speed(in/min)' in object:
                    value = object['speed(in/min)']
                    if value is None:
                        object['speed_min(mm/min)'] = None
                        object['speed_max(mm/min)'] = None
                    elif "~" in value and value is not None:
                        arr = value.split('~')
                        if float(arr[0]) > float(arr[1]):
                            object['speed_min(mm/min)'] = round(float(arr[1])*25.4, 2)
                            object['speed_max(mm/min)'] = round(float(arr[0])*25.4, 2)
                        else:
                            object['speed_min(mm/min)'] = round(float(arr[0])*25.4, 2)
                            object['speed_max(mm/min)'] = round(float(arr[1])*25.4, 2)
                    else:
                        object['speed_min(mm/min)'] = round(float(value)*25.4, 2)
                        object['speed_max(mm/min)'] = round(float(value)*25.4, 2)

                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')