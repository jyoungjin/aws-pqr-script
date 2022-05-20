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
                try:
                    if 'speed(mm/min)' in object and object['speed(mm/min)'] is not None:
                        value = object['speed(mm/min)']
                        if type(value) is str and "~" in value:
                            arr = value.split('~')
                            if float(arr[0]) > float(arr[1]):
                                object['speed_min(mm/min)'] = float(arr[1])
                                object['speed_max(mm/min)'] = float(arr[0])
                            else:
                                object['speed_min(mm/min)'] = float(arr[0])
                                object['speed_max(mm/min)'] = float(arr[1])
                        else:
                            object['speed_min(mm/min)'] = float(value)
                            object['speed_max(mm/min)'] = float(value)

                        with open(file_path, 'w', encoding='utf-8') as mk_f:
                            json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
                except:
                    print(jsonData['pqr_info']['company'])
                    print(jsonData['pqr_info']['procedure_qualification_record_no'])

# for item in counts.keys():
#     print(item, end=', ')