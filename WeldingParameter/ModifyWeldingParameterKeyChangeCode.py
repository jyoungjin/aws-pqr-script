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
                if "speed(mm/min)" in object:
                    if object["speed(mm/min)"] == "" and object["heat_input(kj/mm)"] != "":
                        heatInputVal = float(object["heat_input(kj/mm)"])
                        ampVal = float(object["amps(A)"])
                        voltVal = float(object["volt(V)"])
                        speedVal = (ampVal*voltVal*60)/(1000*heatInputVal)
                        object["speed(mm/min)"] = round(speedVal,2)
                        with open(file_path, 'w', encoding='utf-8') as mk_f:
                            json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
                    elif object["speed(mm/min)"] == "" and object["heat_input(kj/mm)"] == "":
                        object["speed(mm/min)"] = None
                        with open(file_path, 'w', encoding='utf-8') as mk_f:
                            json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')