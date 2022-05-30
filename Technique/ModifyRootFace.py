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
            if 'root_face' in jsonData['joint_design']:
                root_face = jsonData['joint_design']["root_face"]
                if "mm" in root_face:
                    if "~" in root_face:
                        root_face = root_face.strip("mm")
                        arr = root_face.split("~")
                        jsonData['joint_design']['_root_face_min(mm)'] = float(arr[0])
                        jsonData['joint_design']['_root_face_max(mm)'] = float(arr[1])
                    else:
                        root_face = root_face.strip("mm")
                        jsonData['joint_design']['_root_face_min(mm)'] = float(root_face)
                        jsonData['joint_design']['_root_face_max(mm)'] = float(root_face)
                else:
                    jsonData['joint_design']['_root_face_min(mm)'] = None
                    jsonData['joint_design']['_root_face_max(mm)'] = None

                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')