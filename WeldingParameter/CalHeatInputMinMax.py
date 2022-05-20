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
                if 'volt(V)' in object and 'amps(A)' in object and 'speed(mm/min)' in object:
                    amp_min = object['amp_min(A)']
                    amp_max = object['amp_max(A)']
                    volt_min = object['volt_min(V)']
                    volt_max = object['volt_max(V)']
                    speed_min = object['speed_min(mm/min)']
                    speed_max = object['speed_max(mm/min)']

                    heat_input_min = (amp_min*volt_min*60)/(speed_max*1000)
                    heat_input_max = (amp_max*volt_max*60)/(speed_min*1000)


                    object['heat_input_min(kj/mm)'] = round(float(heat_input_min),2)
                    object['heat_input_max(kj/mm)'] = round(float(heat_input_max),2)

                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')