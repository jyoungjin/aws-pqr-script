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
            if 'preheat_temp' in jsonData['preheat']:
                preheat_temp = jsonData['preheat']["preheat_temp"]

                if preheat_temp == "dict":
                    jsonData['preheat']['_min_preheat_temp(°C)'] = {}
                    for key in preheat_temp.keys():
                        tempVal = jsonData['preheat']['preheat_temp'][key]
                        if "°C" in tempVal and len(tempVal) < 10:
                            jsonData['preheat']['_min_preheat_temp(°C)'][key] = float(tempVal.strip('°C'))
                        else:
                            jsonData['preheat']['_min_preheat_temp(°C)'][key] = tempVal
                else:
                    if "°C" in preheat_temp and len(preheat_temp) < 10:
                        jsonData['preheat']['_min_preheat_temp(°C)'] = float(preheat_temp.strip('°C'))
                    else:
                        jsonData['preheat']['_min_preheat_temp(°C)'] = preheat_temp
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')