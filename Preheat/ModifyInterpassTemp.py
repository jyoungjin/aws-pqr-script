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
            if 'interpass_temp' in jsonData['preheat']:
                interpass_temp = jsonData['preheat']["interpass_temp"]

                if interpass_temp == "dict":
                    jsonData['preheat']['_interpass_temp(°C)'] = {}
                    for key in interpass_temp.keys():
                        tempVal = jsonData['preheat']['interpass_temp'][key]
                        if "°C" in tempVal:
                            jsonData['preheat']['_interpass_temp(°C)'][key] = float(tempVal.strip('°C'))
                        else:
                            jsonData['preheat']['_interpass_temp(°C)'][key] = None
                else:
                    if "°C" in interpass_temp:
                        jsonData['preheat']['_interpass_temp(°C)'] = float(interpass_temp.strip('°C'))
                    else:
                        jsonData['preheat']['_interpass_temp(°C)'] = None
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')