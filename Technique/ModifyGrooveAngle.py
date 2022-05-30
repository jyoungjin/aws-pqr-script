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
            if 'groove_angle' in jsonData['joint_design']:
                groove_angle = jsonData['joint_design']["groove_angle"]
                if "°" in groove_angle:
                    if "~" in groove_angle:
                        groove_angle = groove_angle.strip("°")
                        arr = groove_angle.split("~")
                        jsonData['joint_design']['_groove_angle_min(°)'] = float(arr[0])
                        jsonData['joint_design']['_groove_angle_max(°)'] = float(arr[1])
                    else:
                        groove_angle = groove_angle.strip("°")
                        jsonData['joint_design']['_groove_angle_min(°)'] = float(groove_angle)
                        jsonData['joint_design']['_groove_angle_max(°)'] = float(groove_angle)
                else:
                    jsonData['joint_design']['_groove_angle_min(°)'] = None
                    jsonData['joint_design']['_groove_angle_max(°)'] = None

                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')