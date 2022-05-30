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
            if 'shielding_flow_rate' in jsonData['gas']:
                shielding_flow_rate = jsonData['gas']["shielding_flow_rate"]

                if shielding_flow_rate == "dict":
                    jsonData['gas']['_shielding_flow_rate_min(l/min)'] = {}
                    jsonData['gas']['_shielding_flow_rate_max(l/min)'] = {}
                else:
                    if "l/min" in shielding_flow_rate:
                        shielding_flow_rate = shielding_flow_rate.strip('l/min')
                        if "~" in shielding_flow_rate:
                            arr = shielding_flow_rate.split('~')
                            jsonData['gas']['_shielding_flow_rate_min(l/min)'] = float(arr[0])
                            jsonData['gas']['_shielding_flow_rate_max(l/min)'] = float(arr[1])
                        else:
                            jsonData['gas']['_shielding_flow_rate_min(l/min)'] = float(
                                shielding_flow_rate)
                            jsonData['gas']['_shielding_flow_rate_max(l/min)'] = float(
                                shielding_flow_rate)
                    else:
                        jsonData['gas']['_shielding_flow_rate_min(l/min)'] = None
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')