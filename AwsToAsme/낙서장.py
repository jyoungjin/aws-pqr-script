import json
import os

dir_path = "/Users/youngjin/workspace/json-data/aws-to-asme-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                if jsonData['base_metals']['material_spec'] == "A240" and jsonData['base_metals']['type_and_grade'] == "316L":
                    jsonData['base_metals']['_material_spec'] = "A/SA-240"
                    jsonData['base_metals']['_type_and_grade'] = "316L"
                    jsonData['base_metals']['_p_no'] = "8"
                    jsonData['base_metals']['_gr_no'] = "1"
                    jsonData['base_metals']['_to_uns_no'] = "S31603"
                if jsonData['base_metals']['to_material_spec'] == "A240" and jsonData['base_metals']['to_type_and_grade'] == "316L":
                    jsonData['base_metals']['_to_material_spec'] = "A/SA-240"
                    jsonData['base_metals']['_to_type_and_grade'] = "316L"
                    jsonData['base_metals']['_to_p_no'] = "8"
                    jsonData['base_metals']['_to_gr_no'] = "1"
                    jsonData['base_metals']['_to_uns_no'] = "S31603"
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
