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
            if 'thickness' in jsonData['base_metals'] and 'to_thickness' in jsonData['base_metals']:
                thickness = jsonData['base_metals']["thickness"]
                to_thickness = jsonData['base_metals']["to_thickness"]
                if type(thickness) == dict:
                    jsonData['base_metals']["_thickness(mm)"] = {}
                    for key in thickness.keys():
                        thickVal = thickness[key]
                        if thickVal == "N/A":
                            jsonData['base_metals']["_thickness(mm)"][key] = None
                        else:
                            jsonData['base_metals']["_thickness(mm)"][key] = float(thickVal.upper().strip("MM"))
                if type(to_thickness) == dict:
                    jsonData['base_metals']["_to_thickness(mm)"] = {}
                    for key in to_thickness.keys():
                        to_thickVal = to_thickness[key]
                        if to_thickVal == "N/A":
                            jsonData['base_metals']["_to_thickness(mm)"][key] = None
                        else:
                            jsonData['base_metals']["_to_thickness(mm)"][key] = float(to_thickVal.upper().strip("MM"))
                if type(thickness) != dict and type(to_thickness) != dict:
                    if thickness == "N/A":
                        jsonData['base_metals']["_thickness(mm)"] = None
                    else:
                        jsonData['base_metals']["_thickness(mm)"] = float(thickness.upper().strip("MM"))
                    if to_thickness == "N/A":
                        jsonData['base_metals']["_to_thickness(mm)"] = None
                    else:
                        jsonData['base_metals']["_to_thickness(mm)"] = float(to_thickness.upper().strip("MM"))

                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')